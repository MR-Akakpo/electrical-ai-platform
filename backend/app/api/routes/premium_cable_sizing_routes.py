from fastapi import APIRouter

from app.schemas.premium_cable_sizing_schema import PremiumCableSizingRequest

from app.engineering.cable_sizing_premium.cable_sizing_premium_engine import (
    run_premium_cable_sizing
)


router = APIRouter(
    prefix="/engineering/cable-sizing",
    tags=["Premium Cable Sizing"]
)


@router.post("/analysis")
def premium_cable_sizing_analysis(data: PremiumCableSizingRequest):

    return run_premium_cable_sizing(**data.model_dump())
