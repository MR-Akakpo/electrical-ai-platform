from fastapi import APIRouter

from app.schemas.engineering_ai_schema import (
    EngineeringAIRequest
)

from app.ai.engineering_copilot.engineering_ai_engine import (
    generate_engineering_ai_recommendations
)


router = APIRouter(
    prefix="/engineering-ai",
    tags=["Engineering AI Copilot"]
)


@router.post("/recommendations")
def engineering_ai_recommendations(
    data: EngineeringAIRequest
):

    return generate_engineering_ai_recommendations(
        study_type=data.study_type,
        payload=data.payload
    )
