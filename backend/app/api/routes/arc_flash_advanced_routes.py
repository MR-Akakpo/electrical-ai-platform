from fastapi import APIRouter

from app.schemas.arc_flash_advanced_schema import (
    ArcFlashAdvancedRequest
)

from app.engineering.arc_flash_advanced.arc_flash_engine import (
    run_arc_flash_analysis
)


router = APIRouter(
    prefix="/engineering/arc-flash-advanced",
    tags=["Arc Flash Advanced"]
)


@router.post("/analysis")
def arc_flash_analysis(
    data: ArcFlashAdvancedRequest
):

    return run_arc_flash_analysis(
        voltage_v=data.voltage_v,
        bolted_fault_current_ka=data.bolted_fault_current_ka,
        clearing_time_s=data.clearing_time_s,
        working_distance_mm=data.working_distance_mm
    )
