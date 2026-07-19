from fastapi import FastAPI, Request
from app.routers.tasks import router as tasks_router

from app.database.connection import Base, engine
from app.models.task import Task

app = FastAPI() 

app.include_router(tasks_router)

@app.get("/")
def home():
    return {"message": "Bem vindo ao Task Manager AI API"}
    