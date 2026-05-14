from fastapi import APIRouter

from app.schemas.premium_report_schema import (
    PremiumEngineeringReportRequest
)

from app.reporting.premium_report_engine import (
    generate_premium_engineering_report
)

router = APIRouter(
    prefix="/premium-report",
    tags=["Premium Engineering Reports"],
)


@router.post("/generate")
def generate_report(
    request: PremiumEngineeringReportRequest
):

    return generate_premium_engineering_report(
        request.dict()
    )
