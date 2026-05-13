from fastapi import APIRouter

from app.schemas.solar_bess_schema import (
    SolarBESSAnalysisRequest
)

from app.engineering.solar_bess.solar_bess_engine import (
    run_solar_bess_analysis
)


router = APIRouter(
    prefix="/engineering/solar-bess",
    tags=["Solar PV / BESS"]
)


@router.post("/analysis")
def solar_bess_analysis(
    data: SolarBESSAnalysisRequest
):

    return run_solar_bess_analysis(
        module_power_wp=data.module_power_wp,
        number_of_modules=data.number_of_modules,
        inverter_ac_power_kw=data.inverter_ac_power_kw,
        battery_capacity_kwh=data.battery_capacity_kwh,
        critical_load_kw=data.critical_load_kw,
        performance_ratio=data.performance_ratio,
        depth_of_discharge=data.depth_of_discharge
    )
