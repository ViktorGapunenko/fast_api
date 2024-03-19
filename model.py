from typing import Optional
from pydantic import BaseModel


class TaskAddModel(BaseModel):
    name: str
    description: Optional[str] = None


class TaskModel(TaskAddModel):
    id: int
