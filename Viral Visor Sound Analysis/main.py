from fastapi import FastAPI
from Models import test,scripts_model,user_model,articles_model,article_components
import database
from Controllers import audio_controller as AD_C 
from Controllers import registeration_controller as RG_C
from Controllers import login as LG
from fastapi.middleware.cors import CORSMiddleware
from Controllers import article_controller as AR_C

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Allow specific origin(s)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)


# Migrate tables
test.Base.metadata.create_all(bind=database.engine)
scripts_model.Base.metadata.create_all(bind=database.engine)
user_model.Base.metadata.create_all(bind=database.engine)
articles_model.Base.metadata.create_all(bind=database.engine)
article_components.Base.metadata.create_all(bind=database.engine)




@app.get("/")
async def root():
    return {"message":"welcome to Viral Visor Core feature"}


app.include_router(AD_C.router)
app.include_router(RG_C.router)
app.include_router(LG.router)
app.include_router(AR_C.router)



