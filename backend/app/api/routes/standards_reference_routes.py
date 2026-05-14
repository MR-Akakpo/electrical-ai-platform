from fastapi import APIRouter

from app.schemas.standards_reference_schema import StandardsReferenceRequest
from app.engineering.standards.standards_reference_engine import (
    get_standards_for_study,
    list_supported_study_types,
)

router = APIRouter(
    prefix="/engineering-standards",
    tags=["Engineering Standards Reference"],
)


@router.get("/study-types")
def supported_study_types():
    return list_supported_study_types()


@router.post("/resolve")
def resolve_standards(request: StandardsReferenceRequest):
    return get_standards_for_study(request.study_type)
