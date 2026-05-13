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
        daily_consumption_kwh=data.daily_consumption_kwh,
        peak_sun_hours=data.peak_sun_hours,
        module_power_wp=data.module_power_wp,
        module_voc_v=data.module_voc_v,
        module_vmp_v=data.module_vmp_v,
        inverter_ac_power_kw=data.inverter_ac_power_kw,
        inverter_max_dc_voltage_v=data.inverter_max_dc_voltage_v,
        inverter_mppt_min_v=data.inverter_mppt_min_v,
        inverter_mppt_max_v=data.inverter_mppt_max_v,
        battery_capacity_kwh=data.battery_capacity_kwh,
        critical_load_kw=data.critical_load_kw,
        autonomy_days=data.autonomy_days,
        performance_ratio=data.performance_ratio,
        system_losses_percent=data.system_losses_percent,
        depth_of_discharge=data.depth_of_discharge,
        battery_efficiency=data.battery_efficiency,
        temperature_correction_factor=data.temperature_correction_factor,
        system_type=data.system_type,
        has_generator_backup=data.has_generator_backup
    )
