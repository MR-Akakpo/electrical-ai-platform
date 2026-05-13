from pydantic import BaseModel, Field


class TransformerAnalysisRequest(BaseModel):

    transformer_kva: float = Field(gt=0)

    primary_voltage_v: float = Field(gt=0)

    secondary_voltage_v: float = Field(gt=0)

    impedance_percent: float = Field(gt=0)

    connected_load_kw: float = Field(gt=0)

    power_factor: float = Field(gt=0, le=1)

    phase: str = "three"
