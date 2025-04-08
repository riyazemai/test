from fastapi import FastAPI
from app.api.endpoints import flask_service

app = FastAPI(title="FastAPI Service")

app.include_router(flask_service.router, prefix="/api/v1")