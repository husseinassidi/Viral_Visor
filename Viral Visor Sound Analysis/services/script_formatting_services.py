import openai
from dotenv import load_dotenv
import os
import json
from Models.scripts_model import Scripts
from database import SessionLocal
from sqlalchemy.orm import Session

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def format_text_for_script(audio_id,title, audience, goals, keywords, text):

    """
    Formats the given text into script lines with tonality, body language, and unique IDs using GPT-4.
    
    Parameters:
    - title (str): The title of the content.
    - audience (str): The target audience for the content.
    - goals (list of str): Goals to achieve with the content.
    - keywords (list of str): Keywords relevant to the content.
    - text (str): The text to be reformatted.
    
    Returns:
    - dict: JSON object with reformatted text.
    """
    prompt = f"""
    You are an assistant that helps with content creation by reformulating text into script lines. Please consider the following context to provide better insights:

    Title: {title}
    Audience: {audience}
    Goals: {", ".join(goals)}
    Keywords: {", ".join(keywords)}

    Reformat the following text by breaking it into script lines and adding appropriate tonality, body language, and a unique identifier for each line.

    Text:
    {text}

    Provide the output in JSON format, like this:
    [
      {{ "id": 1, "line": "text of the line", "tonality": "description of tonality", "body_language": "description of body language" }},
      {{ "id": 2, "line": "text of the line", "tonality": "description of tonality", "body_language": "description of body language" }},
      ...
    ]
    Make sure each line has a unique integer ID starting from 1. Ensure the JSON is complete and properly formatted.
    """

    try:
        
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an assistant that helps with content creation by reformulating text for script purposes, adding tonality, body language annotations, and unique identifiers in JSON format."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1500  
        )
        
        response_text = response.choices[0].message['content']
        cleaned_text = response_text.replace("```json", "").replace("```", "").strip()
        response_text.replace("```json", "").replace("```", "").strip()
        
        try:
            response_json = json.loads(cleaned_text)
            save_script(audio_id,response_json)
            return response_json
        except json.JSONDecodeError:
            print("Failed to decode JSON response. Here is the cleaned output:")
            return cleaned_text
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def save_script(audio_id, scripts):
    db: Session = SessionLocal()
    try:
        audio_file = db.query(Scripts).filter(Scripts.audio_track_id == audio_id).first()

        if(audio_file):
            return None
        for script_data in scripts:
            script_entry = Scripts(
                line=script_data["line"],
                body_language=script_data["body_language"],
                tonality=script_data["tonality"],
                audio_track_id=audio_id
            )
            db.add(script_entry)
        
        db.commit()

    except Exception as e:
        db.rollback()  
        print(f"An error occurred: {e}")

    finally:
        db.close()


def script_exist(audio_id):
    db: Session = SessionLocal()
    try:
        audio_file = db.query(Scripts).filter(Scripts.audio_track_id == audio_id).first()

        if audio_file:
            return db.query(Scripts).filter(Scripts.audio_track_id == audio_id).all(), True
        
        # If no script is found, return None and False
        return None, False
    
    finally:
        db.close()



