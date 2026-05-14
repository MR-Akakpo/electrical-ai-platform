from fastapi import APIRouter

from app.schemas.intelligent_audit_schema import (
    IntelligentAuditRequest
)

from app.engineering.audit.intelligent_audit_engine import (
    run_intelligent_electrical_audit
)

router = APIRouter(
    prefix="/intelligent-audit",
    tags=["Intelligent Electrical Audit"],
)


@router.post("/run")
def run_audit(
    request: IntelligentAuditRequest
):

    return run_intelligent_electrical_audit(
        request.dict()
    )
