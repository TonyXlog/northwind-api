from fastapi import FastAPI
from app.api.api_v1.endpoints import tasks

app = FastAPI(title="Northwind Task API")

app.include_router(tasks.router, prefix="/api/v1", tags=["tasks"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Northwind API"}

