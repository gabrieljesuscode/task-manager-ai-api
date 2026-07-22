from pydantic import BaseModel, field_validator
from typing import Optional

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = ""



class TaskUpdate(BaseModel):
    title: str
    description: Optional[str] = ""
    completed: bool
    
