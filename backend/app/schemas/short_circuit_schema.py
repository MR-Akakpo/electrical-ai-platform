from pydantic import BaseModel, Field


class ShortCircuitAnalysisRequest(BaseModel):

    transformer_power_kva: float = Field(gt=0)

    voltage_v: float = Field(gt=0)

    impedance_percent: float = Field(gt=0)

    xr_ratio: float = Field(gt=0)

    breaker_capacity_ka: float = Field(gt=0)

    fault_duration_s: float = Field(gt=0)
