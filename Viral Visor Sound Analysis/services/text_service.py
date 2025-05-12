import whisper

def speech_to_text(aud):
    model = whisper.load_model('base')
    
    result = model.transcribe(aud, fp16=False)
    return result["text"]

# Test the function with an audio file
# print(speech_to_text("./Test_files/test.mp3"))
