from pydantic import BaseModel, Field


class MotorAnalysisRequest(BaseModel):

    motor_power_kw: float = Field(gt=0)

    voltage_v: float = Field(gt=0)

    power_factor: float = Field(
        gt=0,
        le=1
    )

    efficiency: float = Field(
        gt=0,
        le=1
    )

    starting_method: str = "DOL"

    generator_kva: float = Field(gt=0)
