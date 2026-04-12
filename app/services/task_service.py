import json
import os
from app.schemas.task import Task, TaskCreate

JSON_FILE = "data/tasks.json"

def read_tasks():
    if not os.path.exists(JSON_FILE):
        return []
    with open(JSON_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(JSON_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(task_in: TaskCreate):
    tasks = read_tasks()
    new_id = len(tasks) + 1

    new_task = task_in.model_dump()
    new_task["id"] = new_id

    tasks.append(new_task)
    save_tasks(tasks)
    return new_task

def delete_task(task_id: int):
    tasks = read_tasks()
    tasks = [t for t in tasks if t["id"] != task_id]
    save_tasks(tasks)

