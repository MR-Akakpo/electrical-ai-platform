from pydantic import BaseModel, Field


class GeneratorAnalysisRequest(BaseModel):

    generator_power_kva: float = Field(gt=0)

    voltage_v: float = Field(gt=0)

    connected_load_kva: float = Field(gt=0)

    largest_motor_kw: float = Field(ge=0)

    fuel_tank_liters: float = Field(gt=0)

    fuel_consumption_lph: float = Field(gt=0)

    number_of_generators: int = Field(gt=0)

    required_generators: int = Field(gt=0)

    application: str = "general"

    generator_type: str = "diesel"
