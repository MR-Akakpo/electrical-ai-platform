from pydantic import BaseModel, Field


class DCSystemAnalysisRequest(BaseModel):

    dc_voltage_v: float = Field(gt=0)

    dc_power_w: float = Field(gt=0)

    battery_capacity_ah: float = Field(gt=0)

    rectifier_module_current_a: float = Field(gt=0)
