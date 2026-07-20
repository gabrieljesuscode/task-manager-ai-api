from fastapi import FastAPI
from app.routers.tasks import router as tasks_router
from app.routers.ai import router as ai_categorize_router

app = FastAPI() 

app.include_router(tasks_router)
app.include_router(ai_categorize_router)

@app.get("/")
def home():
    return {"message": "Bem vindo ao Task Manager AI API"}
