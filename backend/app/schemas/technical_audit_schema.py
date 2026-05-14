from pydantic import BaseModel


class AuditItem(BaseModel):

    category: str

    requirement: str

    status: str

    severity: str = "medium"

    comment: str = ""


class TechnicalAuditEvaluationRequest(BaseModel):

    project_name: str

    auditor_name: str

    site_name: str

    audit_items: list[AuditItem]


class TechnicalAuditExportRequest(BaseModel):

    file_name: str

    export_format: str = "pdf"

    audit_data: dict

    include_logo_1: bool = False

    logo_1_path: str | None = None

    include_logo_2: bool = False

    logo_2_path: str | None = None
