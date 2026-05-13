from fastapi import APIRouter

from app.schemas.busbar_schema import (
    BusbarAnalysisRequest
)

from app.engineering.busbars.busbar_engine import (
    run_busbar_analysis
)


router = APIRouter(
    prefix="/engineering/busbars",
    tags=["Busbars / Jeux de barres"]
)


@router.post("/analysis")
def busbar_analysis(
    data: BusbarAnalysisRequest
):

    return run_busbar_analysis(
        rated_current_a=data.rated_current_a,
        busbar_section_mm2=data.busbar_section_mm2,
        material=data.material,
        short_circuit_current_ka=data.short_circuit_current_ka,
        withstand_current_ka=data.withstand_current_ka,
        peak_fault_current_ka=data.peak_fault_current_ka,
        peak_withstand_ka=data.peak_withstand_ka,
        duration_s=data.duration_s
    )
