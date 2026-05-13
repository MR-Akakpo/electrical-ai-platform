from pydantic import BaseModel, Field


class HarmonicAnalysisRequest(BaseModel):

    thdi_percent: float = Field(ge=0)

    thdv_percent: float = Field(ge=0)

    harmonic_k_factor: float = Field(ge=1)

    single_phase_nonlinear_load_ratio_percent: float = Field(ge=0, le=100)

    has_vfd: bool = False

    has_ups: bool = False
