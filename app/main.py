import os
from dotenv import load_dotenv
load_dotenv()


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.tasks import router as tasks_router
from app.routers.ai import router as ai_categorize_router

from app.database.connection import engine, Base
import app.models.task

app = FastAPI() 

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        os.getenv("WEB_URL")
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tasks_router)
app.include_router(ai_categorize_router)

@app.get("/")
def home():
    return {"message": "Bem vindo ao Task Manager AI API"}
