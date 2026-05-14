from fastapi import APIRouter

from app.schemas.report_schema import (
    EngineeringReportRequest
)

from app.engineering.reports.report_engine import (
    generate_engineering_report
)


router = APIRouter(
    prefix="/reports",
    tags=["Engineering Reports"]
)


@router.post("/generate")
def generate_report(
    data: EngineeringReportRequest
):

    return generate_engineering_report(
        project_name=data.project_name,
        study_type=data.study_type,
        title=data.title,
        input_data=data.input_data,
        result_data=data.result_data,
        recommendations=data.recommendations,
        standard=data.standard
    )
