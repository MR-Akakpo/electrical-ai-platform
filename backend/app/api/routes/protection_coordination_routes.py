from fastapi import APIRouter

from app.schemas.protection_coordination_schema import (
    ProtectionCoordinationRequest
)

from app.engineering.protection_coordination.protection_coordination_engine import (
    run_protection_coordination_analysis
)


router = APIRouter(
    prefix="/engineering/protection-coordination",
    tags=["Protection Coordination / Selectivity"]
)


@router.post("/analysis")
def protection_coordination_analysis(
    data: ProtectionCoordinationRequest
):

    return run_protection_coordination_analysis(
        upstream_breaker_rating_a=data.upstream_breaker_rating_a,
        downstream_breaker_rating_a=data.downstream_breaker_rating_a,
        upstream_trip_time_s=data.upstream_trip_time_s,
        downstream_trip_time_s=data.downstream_trip_time_s,
        upstream_breaking_capacity_ka=data.upstream_breaking_capacity_ka,
        downstream_fault_level_ka=data.downstream_fault_level_ka,
        application=data.application,
        criticality=data.criticality
    )
