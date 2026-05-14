from fastapi import APIRouter

from app.schemas.ups_schema import (
    UPSAnalysisRequest
)

from app.engineering.ups.ups_engine import (
    run_ups_analysis
)


router = APIRouter(
    prefix="/engineering/ups",
    tags=["UPS Systems"]
)


@router.post("/analysis")
def ups_analysis(
    data: UPSAnalysisRequest
):

    return run_ups_analysis(
        ups_power_kva=data.ups_power_kva,
        connected_load_kva=data.connected_load_kva,
        connected_load_kw=data.connected_load_kw,
        battery_voltage_v=data.battery_voltage_v,
        battery_capacity_ah=data.battery_capacity_ah,
        dc_bus_efficiency=data.dc_bus_efficiency,
        redundancy_type=data.redundancy_type,
        has_static_bypass=data.has_static_bypass,
        has_maintenance_bypass=data.has_maintenance_bypass,
        application=data.application,
        battery_type=data.battery_type
    )
