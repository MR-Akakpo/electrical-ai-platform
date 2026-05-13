from pydantic import BaseModel, Field


class GeneratorAnalysisRequest(BaseModel):

    total_load_kw: float = Field(gt=0)

    power_factor: float = Field(gt=0, le=1)

    motor_start_kva: float = Field(ge=0)

    fuel_tank_liters: float = Field(ge=0)

    fuel_consumption_lph: float = Field(gt=0)

    load_type: str = "mixed"

    redundancy_type: str = "N+1"


class GeneratorAnalysisResponse(BaseModel):

    required_generator_kva: float

    base_generator_kva: float

    voltage_dip_percent: float

    transient_analysis: str

    fuel_autonomy_hours: float

    redundancy_type: str

    recommendations: list[str]
