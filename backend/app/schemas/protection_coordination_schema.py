from pydantic import BaseModel, Field


class ProtectionCoordinationRequest(BaseModel):

    upstream_breaker_a: float = Field(gt=0)

    downstream_breaker_a: float = Field(gt=0)

    upstream_icu_ka: float = Field(gt=0)

    downstream_fault_ka: float = Field(gt=0)

    breaker_curve: str = "C"

    load_inrush_multiple: float = Field(gt=0)
