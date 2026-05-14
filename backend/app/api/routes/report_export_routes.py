from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.schemas.premium_report_schema import (
    PremiumEngineeringReportRequest
)

from app.reporting.premium_report_engine import (
    generate_premium_engineering_report
)

from app.reporting.report_export_engine import (
    build_pdf_report,
    build_docx_report,
)

router = APIRouter(
    prefix="/premium-report-export",
    tags=["Premium Report Export"],
)


@router.post("/pdf")
def export_pdf(
    request: PremiumEngineeringReportRequest
):

    report = generate_premium_engineering_report(
        request.dict()
    )

    pdf_buffer = build_pdf_report(
        report
    )

    return StreamingResponse(
        pdf_buffer,
        media_type="application/pdf",
        headers={
            "Content-Disposition":
            "attachment; filename=engineering_report.pdf"
        }
    )


@router.post("/docx")
def export_docx(
    request: PremiumEngineeringReportRequest
):

    report = generate_premium_engineering_report(
        request.dict()
    )

    docx_buffer = build_docx_report(
        report
    )

    return StreamingResponse(
        docx_buffer,
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        headers={
            "Content-Disposition":
            "attachment; filename=engineering_report.docx"
        }
    )
