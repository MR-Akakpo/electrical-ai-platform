from pydantic import BaseModel, Field


class PowerQualityRequest(BaseModel):

    thdi_percent: float = Field(ge=0)

    thdv_percent: float = Field(ge=0)

    nonlinear_load_ratio_percent: float = Field(
        ge=0,
        le=100
    )

    ambient_temperature_c: float = Field(
        ge=-20,
        le=80
    )
