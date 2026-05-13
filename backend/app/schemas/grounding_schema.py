from pydantic import BaseModel, Field


class GroundingAnalysisRequest(BaseModel):

    earthing_system: str = "TN-S"

    fault_current_a: float = Field(gt=0)

    earth_resistance_ohm: float = Field(gt=0)

    touch_voltage_limit_v: float = Field(default=50, gt=0)
