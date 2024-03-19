from typing import Annotated
from fastapi import Depends, APIRouter
from model import TaskAddModel
from repository import TaskRepository


router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.post("/")
async def add_task(
    task: Annotated[TaskAddModel, Depends()],
):
    task_id = await TaskRepository.add_one(task)
    return {"task_id": task_id}


@router.get("/")
async def get_tasks():
    tasks = await TaskRepository.find_all()
    return tasks
