from fastapi import APIRouter

from app.schemas.export_schema import (
    EngineeringExportRequest
)

from app.engineering.exports.export_engine import (
    export_engineering_report
)


router = APIRouter(
    prefix="/exports",
    tags=["Engineering Exports"]
)


@router.post("/report")
def export_report(
    data: EngineeringExportRequest
):

    return export_engineering_report(
        file_name=data.file_name,
        report_data=data.report_data,
        export_format=data.export_format
    )
