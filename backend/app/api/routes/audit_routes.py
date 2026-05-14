from fastapi import APIRouter

from app.schemas.audit_schema import (
    EngineeringAuditRequest
)

from app.engineering.audit.audit_engine import (
    audit_project_consistency
)


router = APIRouter(
    prefix="/audit",
    tags=["Engineering Audit"]
)


@router.post("/project-consistency")
def project_consistency_audit(
    data: EngineeringAuditRequest
):

    return audit_project_consistency(
        project_name=data.project_name,
        studies=data.studies,
        networks=data.networks
    )
