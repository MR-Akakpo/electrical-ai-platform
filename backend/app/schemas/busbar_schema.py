from pydantic import BaseModel, Field


class BusbarAnalysisRequest(BaseModel):

    rated_current_a: float = Field(gt=0)

    busbar_section_mm2: float = Field(gt=0)

    material: str = "copper"

    short_circuit_current_ka: float = Field(ge=0)

    withstand_current_ka: float = Field(ge=0)

    peak_fault_current_ka: float = Field(ge=0)

    peak_withstand_ka: float = Field(ge=0)

    duration_s: float = Field(default=1, gt=0)
