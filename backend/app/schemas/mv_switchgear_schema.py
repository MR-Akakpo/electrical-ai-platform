from pydantic import BaseModel, Field


class MVSwitchgearAnalysisRequest(BaseModel):

    application: str

    rated_voltage_kv: float = Field(gt=0)

    rated_current_a: float = Field(gt=0)

    short_circuit_level_ka: float = Field(ge=0)

    earthing_system: str = "IT"

    indoor: bool = True
