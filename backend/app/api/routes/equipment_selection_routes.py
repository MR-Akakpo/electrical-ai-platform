from fastapi import APIRouter

from app.schemas.equipment_selection_schema import (
    EngineeringEquipmentRecommendationRequest
)

from app.engineering.equipment_selection_engine import (
    build_engineering_recommendation
)

router = APIRouter(
    prefix="/equipment-selection",
    tags=["Engineering Equipment Selection"],
)


@router.post("/recommend")
def recommend_equipment(
    request: EngineeringEquipmentRecommendationRequest
):

    return build_engineering_recommendation(
        request.current_a,
        request.material
    )
