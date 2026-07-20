from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session 

from app.schemas.task import TaskCreate, TaskUpdate
from app.database.connection import get_db
from app.models.task import Task

from app.ai.service import categorize_tasks


router = APIRouter()


def make_task_string(index: int, task: Task):
    return f"Tarefa{index}: \nTítulo Da Tarefa: {task.title}. \nExplicação da Tarefa: {task.description}"

@router.get("/ai/categorize")
def get_categories(db: Session = Depends(get_db)):

    tasks = db.query(Task).all()
    
    if not tasks:
        raise HTTPException(
            status_code=404,
            detail="No tasks found."
        )
    
    tasks_string = [make_task_string(index, task) for index, task in enumerate(tasks, start=1)]


    tasks_string = ", ".join(tasks_string)

    print(tasks_string)
    
    categories = categorize_tasks(tasks_string)

    return categories


