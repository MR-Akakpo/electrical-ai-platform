from fastapi import APIRouter

from app.schemas.harmonic_schema import (
    HarmonicAnalysisRequest
)

from app.engineering.harmonics.harmonic_engine import (
    run_harmonic_analysis
)


router = APIRouter(
    prefix="/engineering/harmonics",
    tags=["Harmonics / Power Quality"]
)


@router.post("/analysis")
def harmonic_analysis(
    data: HarmonicAnalysisRequest
):

    return run_harmonic_analysis(
        thdi_percent=data.thdi_percent,
        thdv_percent=data.thdv_percent,
        harmonic_k_factor=data.harmonic_k_factor,
        single_phase_nonlinear_load_ratio_percent=data.single_phase_nonlinear_load_ratio_percent,
        has_vfd=data.has_vfd,
        has_ups=data.has_ups
    )
