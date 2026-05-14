from fastapi import APIRouter

from app.schemas.protection_coordination_advanced_schema import (
    ProtectionCoordinationAdvancedRequest
)

from app.engineering.protection_coordination_advanced.protection_coordination_engine import (
    run_protection_coordination_advanced_analysis
)


router = APIRouter(
    prefix="/engineering/protection-coordination-advanced",
    tags=["Protection Coordination Advanced"]
)


@router.post("/analysis")
def protection_coordination_advanced_analysis(
    data: ProtectionCoordinationAdvancedRequest
):

    return run_protection_coordination_advanced_analysis(
        upstream_trip_time_s=data.upstream_trip_time_s,
        downstream_trip_time_s=data.downstream_trip_time_s,
        upstream_current_a=data.upstream_current_a,
        downstream_current_a=data.downstream_current_a,
        upstream_breaking_capacity_ka=data.upstream_breaking_capacity_ka,
        prospective_fault_current_ka=data.prospective_fault_current_ka,
        installation_type=data.installation_type
    )
