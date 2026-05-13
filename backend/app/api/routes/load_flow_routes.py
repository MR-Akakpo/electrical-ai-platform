from fastapi import APIRouter

from app.schemas.load_flow_schema import (
    LoadFlowAnalysisRequest
)

from app.engineering.load_flow.load_flow_engine import (
    run_load_flow_analysis
)


router = APIRouter(
    prefix="/engineering/load-flow",
    tags=["Load Flow / Power Balance"]
)


@router.post("/analysis")
def load_flow_analysis(
    data: LoadFlowAnalysisRequest
):

    loads = [
        item.model_dump()
        for item in data.loads
    ]

    return run_load_flow_analysis(
        loads=loads,
        source_capacity_kva=data.source_capacity_kva,
        voltage_v=data.voltage_v,
        phase=data.phase
    )
