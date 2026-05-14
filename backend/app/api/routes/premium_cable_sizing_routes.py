from fastapi import APIRouter

from app.schemas.premium_cable_sizing_schema import (
    PremiumCableSizingRequest
)

from app.engineering.cable_sizing_premium.cable_sizing_premium_engine import (
    run_premium_cable_sizing
)


router = APIRouter(
    prefix="/engineering/cable-sizing",
    tags=["Premium Cable Sizing"]
)


@router.post("/analysis")
def premium_cable_sizing_analysis(
    data: PremiumCableSizingRequest
):

    return run_premium_cable_sizing(
        power_kw=data.power_kw,
        power_kva=data.power_kva,
        current_a=data.current_a,
        power_input_type=data.power_input_type,
        voltage_v=data.voltage_v,
        power_factor=data.power_factor,
        system_type=data.system_type,
        current_type=data.current_type,
        conductor_material=data.conductor_material,
        insulation_type=data.insulation_type,
        installation_method=data.installation_method,
        ambient_temperature_c=data.ambient_temperature_c,
        grouped_circuits=data.grouped_circuits,
        cable_length_m=data.cable_length_m,
        max_voltage_drop_percent=data.max_voltage_drop_percent,
        fault_current_ka=data.fault_current_ka,
        fault_duration_s=data.fault_duration_s,
        earthing_system=data.earthing_system,
        load_type=data.load_type,
        thdi_percent=data.thdi_percent,
        future_margin_percent=data.future_margin_percent,
        efficiency=data.efficiency,
        parallel_cables=data.parallel_cables
    )
