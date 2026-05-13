from fastapi import APIRouter

from app.schemas.switchboard_schema import (
    SwitchboardAnalysisRequest
)

from app.engineering.switchboards.switchboard_engine import (
    run_switchboard_analysis
)


router = APIRouter(
    prefix="/engineering/switchboards",
    tags=["Switchboards / TGBT"]
)


@router.post("/analysis")
def switchboard_analysis(
    data: SwitchboardAnalysisRequest
):

    return run_switchboard_analysis(
        application=data.application,
        rated_current_a=data.rated_current_a,
        short_circuit_level_ka=data.short_circuit_level_ka,
        duration_s=data.duration_s,
        environment=data.environment,
        criticality=data.criticality,
        maintenance_requirement=data.maintenance_requirement
    )
