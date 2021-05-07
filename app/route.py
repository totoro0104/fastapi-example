from fastapi import APIRouter

from app import auth
from app.api import test_api

api_router = APIRouter()
api_router.include_router(test_api.router, tags=["test"])
api_router.include_router(auth.router, tags=["auth"])
