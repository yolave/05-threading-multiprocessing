from fastapi import APIRouter
from ..api.endpoints import users
from ..api.endpoints import concurrency

router = APIRouter()
router.include_router(users.router, prefix="/users", tags=["Users"])
router.include_router(concurrency.router, prefix="/concurrency", tags=["Concurrency"])
