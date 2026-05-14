from fastapi import APIRouter

from app.core.health.health_service import (
    get_backend_health
)


router = APIRouter(
    prefix="/health",
    tags=["System Health"]
)


@router.get("/")
def health_check():

    return get_backend_health()
