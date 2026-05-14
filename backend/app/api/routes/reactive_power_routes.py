from fastapi import APIRouter

from app.schemas.reactive_power_schema import (
    ReactivePowerAnalysisRequest
)

from app.engineering.reactive_power.reactive_power_engine import (
    run_reactive_power_analysis
)


router = APIRouter(
    prefix="/engineering/reactive-power",
    tags=["Reactive Power Compensation"]
)


@router.post("/analysis")
def reactive_power_analysis(
    data: ReactivePowerAnalysisRequest
):

    return run_reactive_power_analysis(
        active_power_kw=data.active_power_kw,
        initial_power_factor=data.initial_power_factor,
        target_power_factor=data.target_power_factor,
        has_harmonics=data.has_harmonics,
        load_variation=data.load_variation
    )
