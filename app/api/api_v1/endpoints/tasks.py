from fastapi import APIRouter
from app.schemas.task import Task, TaskCreate
from app.services import task_service


router = APIRouter()

@router.get("/")
def get_tasks():
    return task_service.read_tasks()

@router.post("/")
def create_task(task: TaskCreate):
    return task_service.add_task(task)

@router.delete("/{task_id}")
def delete_task(task_id: int):
    return task_service.delete_task(task_id)
