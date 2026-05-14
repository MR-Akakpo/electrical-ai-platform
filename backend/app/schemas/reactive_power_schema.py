from pydantic import BaseModel, Field


class ReactivePowerAnalysisRequest(BaseModel):

    active_power_kw: float = Field(gt=0)

    initial_power_factor: float = Field(gt=0, lt=1)

    target_power_factor: float = Field(gt=0, le=1)

    has_harmonics: bool = False

    load_variation: str = "variable"


class ReactivePowerRequest(BaseModel):

    active_power_kw: float = Field(gt=0)

    initial_power_factor: float = Field(gt=0, lt=1)

    target_power_factor: float = Field(gt=0, le=1)

    harmonic_environment: bool = False

    generator_present: bool = False

    generator_kva: float = Field(default=0, ge=0)

    thdi_percent: float = Field(default=0, ge=0)
