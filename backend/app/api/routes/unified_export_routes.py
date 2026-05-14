from fastapi import APIRouter

from app.schemas.unified_export_schema import (
    UnifiedExportRequest
)

from app.engineering.unified_exports.unified_export_engine import (
    build_engineering_pdf_report
)

router = APIRouter(
    prefix="/unified-exports",
    tags=["Unified Engineering Exports"],
)


@router.post("/pdf")
def export_pdf(
    request: UnifiedExportRequest
):

    return build_engineering_pdf_report(
        title=request.title,
        project_name=request.project_name,
        sections=[
            section.dict()
            for section in request.sections
        ],
    )
