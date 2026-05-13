from fastapi import APIRouter

from app.schemas.dc_system_schema import (
    DCSystemAnalysisRequest
)

from app.engineering.dc_systems.dc_system_engine import (
    run_dc_system_analysis
)


router = APIRouter(
    prefix="/engineering/dc-systems",
    tags=["DC Systems / Rectifiers"]
)


@router.post("/analysis")
def dc_system_analysis(
    data: DCSystemAnalysisRequest
):

    return run_dc_system_analysis(
        dc_voltage_v=data.dc_voltage_v,
        dc_power_w=data.dc_power_w,
        battery_capacity_ah=data.battery_capacity_ah,
        rectifier_module_current_a=data.rectifier_module_current_a
    )
