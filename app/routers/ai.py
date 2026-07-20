from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session 

from app.schemas.task import TaskCreate, TaskUpdate
from app.database.connection import get_db
from app.models.task import Task

from app.ai.service import categorize_tasks


router = APIRouter()


@router.get("/ai/categorize")
def get_categories(db: Session = Depends(get_db)):

    tasks = db.query(Task).all()
    
    if not tasks:
        raise HTTPException(
            status_code=404,
            detail="No tasks found."
        )
    
    
    categories = categorize_tasks(tasks)

    return categories


