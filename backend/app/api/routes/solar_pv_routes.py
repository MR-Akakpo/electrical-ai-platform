from fastapi import APIRouter

from app.schemas.solar_pv_schema import (
    SolarPVAnalysisRequest
)

from app.engineering.solar_pv.solar_pv_engine import (
    run_solar_pv_analysis
)


router = APIRouter(
    prefix="/engineering/solar-pv",
    tags=["Solar PV"]
)


@router.post("/analysis")
def solar_pv_analysis(
    data: SolarPVAnalysisRequest
):

    return run_solar_pv_analysis(
        load_power_kw=data.load_power_kw,
        operating_hours_per_day=data.operating_hours_per_day,
        peak_sun_hours=data.peak_sun_hours,
        system_efficiency=data.system_efficiency,
        autonomy_days=data.autonomy_days,
        battery_voltage_v=data.battery_voltage_v,
        depth_of_discharge=data.depth_of_discharge,
        inverter_power_kw=data.inverter_power_kw,
        has_generator_backup=data.has_generator_backup,
        has_grid_connection=data.has_grid_connection,
        has_battery_storage=data.has_battery_storage
    )
