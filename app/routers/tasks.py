from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session 

from app.schemas.task import TaskCreate, TaskUpdate
from app.database.connection import get_db
from app.models.task import Task

router = APIRouter()


@router.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):

    tasks = db.query(Task).order_by(Task.id.desc()).all()

    return tasks



@router.get("/tasks/{task_id}")
def get_one_task(task_id: int, db: Session = Depends(get_db)):

    task = db.get(Task, task_id)


    if not task:
        raise HTTPException(
            status_code=404,
            detail="Tarefa não encontrada"   
        )
    
    return task 



@router.post("/tasks", status_code=201)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    if not task.title or task.title == "":
        raise HTTPException(
            status_code=404,
            detail="Título da tarefa não adicionado"   
        )
    
    new_task = Task(
        title= task.title,
        description=task.description,
        completed=False
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task


@router.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskUpdate, db: Session = Depends(get_db)):

    existing_task = db.get(Task, task_id)

    if not existing_task:
        raise HTTPException(
            status_code=404,
            detail="Tarefa não encontrada"   
        )
    
    existing_task.title = task.title
    existing_task.description = task.description
    existing_task.completed = task.completed


    db.commit()
    db.refresh(existing_task)

    
    return existing_task





@router.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    
    existing_task = db.get(Task, task_id)

    
    if not existing_task:
        raise HTTPException(
            status_code=404,
            detail="Tarefa não encontrada"   
        )
    
    db.delete(existing_task)
    db.commit()
