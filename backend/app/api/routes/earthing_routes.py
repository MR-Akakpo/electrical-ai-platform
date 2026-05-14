from fastapi import APIRouter

from app.schemas.earthing_schema import (
    EarthingAnalysisRequest
)

from app.engineering.earthing.earthing_engine import (
    run_earthing_analysis
)


router = APIRouter(
    prefix="/engineering/earthing",
    tags=["Earthing / Grounding"]
)


@router.post("/analysis")
def earthing_analysis(
    data: EarthingAnalysisRequest
):

    return run_earthing_analysis(
        earth_resistance_ohm=data.earth_resistance_ohm,
        earthing_system=data.earthing_system,
        installation_type=data.installation_type,
        fault_current_a=data.fault_current_a,
        lightning_protection_required=data.lightning_protection_required
    )
