from fastapi import APIRouter

from app.schemas.unified_workflow_schema import (
    UnifiedEngineeringWorkflowRequest
)

from app.engineering.unified_engineering_workflow import (
    build_unified_engineering_workflow
)

router = APIRouter(
    prefix="/engineering-workflow",
    tags=["Unified Engineering Workflow"],
)


@router.post("/run")
def run_workflow(
    request: UnifiedEngineeringWorkflowRequest
):

    return build_unified_engineering_workflow(
        request.dict()
    )
