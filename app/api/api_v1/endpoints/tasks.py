from fastapi import APIRouter
from app.schemas.task import Task, TaskCreate, TaskStatusUpdate
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

@router.patch("/{task_id}")
def patch_status(task_id: int, task_status: TaskStatusUpdate):
    return task_service.update_status(task_id, task_status)