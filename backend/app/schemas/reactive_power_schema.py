from pydantic import BaseModel, Field


class ReactivePowerAnalysisRequest(BaseModel):

    active_power_kw: float = Field(gt=0)

    initial_power_factor: float = Field(gt=0, lt=1)

    target_power_factor: float = Field(gt=0, le=1)

    has_harmonics: bool = False

    load_variation: str = "variable"
