from pydantic import BaseModel, Field


class MotorAnalysisRequest(BaseModel):

    motor_power_kw: float = Field(gt=0)

    voltage_v: float = Field(gt=0)

    efficiency: float = Field(gt=0, le=1)

    power_factor: float = Field(gt=0, le=1)

    connected_load_kw: float = Field(gt=0)

    starting_method: str = "DOL"

    criticality: str = "standard"

    application: str = "general"
