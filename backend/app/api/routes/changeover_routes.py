from fastapi import APIRouter

from app.schemas.changeover_schema import (
    ChangeoverAnalysisRequest
)

from app.engineering.changeover.changeover_engine import (
    run_changeover_analysis
)


router = APIRouter(
    prefix="/engineering/changeover",
    tags=["ATS / STS / Changeover"]
)


@router.post("/analysis")
def changeover_analysis(
    data: ChangeoverAnalysisRequest
):

    return run_changeover_analysis(
        application=data.application,
        source_1_type=data.source_1_type,
        source_2_type=data.source_2_type,
        rated_current_a=data.rated_current_a,
        load_type=data.load_type,
        criticality=data.criticality,
        transfer_time_s=data.transfer_time_s,
        closed_transition=data.closed_transition
    )
