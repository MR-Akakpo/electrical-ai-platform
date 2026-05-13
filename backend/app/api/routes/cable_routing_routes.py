from fastapi import APIRouter

from app.schemas.cable_routing_schema import (
    CableRoutingAnalysisRequest
)

from app.engineering.cable_routing.cable_routing_engine import (
    run_cable_routing_analysis
)


router = APIRouter(
    prefix="/engineering/cable-routing",
    tags=["Cable Routing / Trays"]
)


@router.post("/analysis")
def cable_routing_analysis(
    data: CableRoutingAnalysisRequest
):

    return run_cable_routing_analysis(
        total_cable_area_mm2=data.total_cable_area_mm2,
        tray_width_mm=data.tray_width_mm,
        tray_height_mm=data.tray_height_mm,
        has_power_cables=data.has_power_cables,
        has_control_cables=data.has_control_cables,
        has_communication_cables=data.has_communication_cables,
        has_vfd_cables=data.has_vfd_cables,
        environment=data.environment,
        fire_safety_required=data.fire_safety_required,
        outdoor=data.outdoor
    )
