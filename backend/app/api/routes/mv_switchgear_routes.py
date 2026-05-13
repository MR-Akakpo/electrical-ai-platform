from fastapi import APIRouter

from app.schemas.mv_switchgear_schema import (
    MVSwitchgearAnalysisRequest
)

from app.engineering.mv_switchgear.mv_switchgear_engine import (
    run_mv_switchgear_analysis
)


router = APIRouter(
    prefix="/engineering/mv-switchgear",
    tags=["MV Switchgear / Cellules HTA"]
)


@router.post("/analysis")
def mv_switchgear_analysis(
    data: MVSwitchgearAnalysisRequest
):

    return run_mv_switchgear_analysis(
        application=data.application,
        rated_voltage_kv=data.rated_voltage_kv,
        rated_current_a=data.rated_current_a,
        short_circuit_level_ka=data.short_circuit_level_ka,
        earthing_system=data.earthing_system,
        indoor=data.indoor
    )
