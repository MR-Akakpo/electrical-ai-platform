from fastapi import APIRouter

from app.schemas.sld_schema import (
    SLDAnalysisRequest
)

from app.engineering.sld.sld_engine import (
    run_sld_analysis
)


router = APIRouter(
    prefix="/engineering/sld",
    tags=["Single Line Diagram"]
)


@router.post("/analysis")
def sld_analysis(
    data: SLDAnalysisRequest
):

    return run_sld_analysis(
        utility_voltage_v=data.utility_voltage_v,
        transformer_power_kva=data.transformer_power_kva,
        generator_power_kva=data.generator_power_kva,
        ups_power_kva=data.ups_power_kva,
        main_switchboard_power_kva=data.main_switchboard_power_kva
    )
