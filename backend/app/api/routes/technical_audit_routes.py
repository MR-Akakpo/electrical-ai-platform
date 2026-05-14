from fastapi import APIRouter

from app.schemas.technical_audit_schema import (
    TechnicalAuditEvaluationRequest,
    TechnicalAuditExportRequest
)

from app.engineering.technical_audit.technical_audit_engine import (
    get_technical_audit_checklist,
    evaluate_technical_audit,
    export_technical_audit
)


router = APIRouter(
    prefix="/technical-audit",
    tags=["Technical Electrical Audit"]
)


@router.get("/checklist")
def technical_audit_checklist():

    return get_technical_audit_checklist()


@router.post("/evaluate")
def technical_audit_evaluate(
    data: TechnicalAuditEvaluationRequest
):

    audit_items = [
        item.model_dump()
        for item in data.audit_items
    ]

    return evaluate_technical_audit(
        project_name=data.project_name,
        auditor_name=data.auditor_name,
        site_name=data.site_name,
        audit_items=audit_items
    )


@router.post("/export")
def technical_audit_export(
    data: TechnicalAuditExportRequest
):

    return export_technical_audit(
        audit_data=data.audit_data,
        file_name=data.file_name,
        export_format=data.export_format,
        include_logo_1=data.include_logo_1,
        logo_1_path=data.logo_1_path,
        include_logo_2=data.include_logo_2,
        logo_2_path=data.logo_2_path
    )
