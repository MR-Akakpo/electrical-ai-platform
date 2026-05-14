from fastapi import APIRouter

from app.schemas.premium_report_schema import (
    PremiumReportRequest
)

from app.engineering.premium_reports.premium_report_engine import (
    export_premium_report
)


router = APIRouter(
    prefix="/premium-reports",
    tags=["Premium Reports"]
)


@router.post("/export")
def premium_report_export(
    data: PremiumReportRequest
):

    sections = [
        section.model_dump()
        for section in data.sections
    ]

    return export_premium_report(
        file_name=data.file_name,
        report_title=data.report_title,
        project_name=data.project_name,
        company_name=data.company_name,
        sections=sections,
        export_format=data.export_format,
        logos=data.logos
    )
