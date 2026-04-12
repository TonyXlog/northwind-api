from fastapi import FastAPI
from app.api.api_v1.endpoints import tasks
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI(title="Northwind Task API")

app.include_router(tasks.router, prefix="/api/v1/tasks", tags=["tasks"])

app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/")
async def read_index():
    return FileResponse('app/static/index.html')

