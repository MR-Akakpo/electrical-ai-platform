from fastapi import APIRouter

from app.schemas.arc_flash_schema import (
    ArcFlashAnalysisRequest
)

from app.engineering.arc_flash.arc_flash_engine import (
    run_arc_flash_analysis
)


router = APIRouter(
    prefix="/engineering/arc-flash",
    tags=["Arc Flash / Electrical Safety"]
)


@router.post("/analysis")
def arc_flash_analysis(
    data: ArcFlashAnalysisRequest
):

    return run_arc_flash_analysis(
        fault_current_ka=data.fault_current_ka,
        clearing_time_s=data.clearing_time_s,
        working_distance_mm=data.working_distance_mm,
        system_voltage_v=data.system_voltage_v,
        equipment_type=data.equipment_type
    )
