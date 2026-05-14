from fastapi import APIRouter

from app.schemas.motor_schema import (
    MotorAnalysisRequest
)

from app.engineering.motors.motor_engine import (
    run_motor_analysis
)


router = APIRouter(
    prefix="/engineering/motors",
    tags=["Motors"]
)


@router.post("/analysis")
def motor_analysis(
    data: MotorAnalysisRequest
):

    return run_motor_analysis(
        motor_power_kw=data.motor_power_kw,
        voltage_v=data.voltage_v,
        efficiency=data.efficiency,
        power_factor=data.power_factor,
        connected_load_kw=data.connected_load_kw,
        starting_method=data.starting_method,
        criticality=data.criticality,
        application=data.application
    )
