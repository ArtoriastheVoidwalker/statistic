from fastapi import APIRouter
from .endpoints import (
    statistic
)

api_router = APIRouter()

api_router.include_router(statistic.router, prefix="/statistics", tags=["statistics"])
