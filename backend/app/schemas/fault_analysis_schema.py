from pydantic import BaseModel, Field


class FaultAnalysisRequest(BaseModel):

    transformer_kva: float = Field(gt=0)

    transformer_voltage_v: float = Field(gt=0)

    transformer_impedance_percent: float = Field(gt=0)

    generator_kva: float = Field(ge=0)

    generator_voltage_v: float = Field(gt=0)

    generator_xdpp_percent: float = Field(gt=0)

    xr_ratio: float = Field(gt=0)

    cable_section_mm2: float = Field(gt=0)

    cable_k_factor: float = Field(gt=0)

    fault_duration_s: float = Field(gt=0)
