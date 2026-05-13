from pydantic import BaseModel, Field


class LoadItem(BaseModel):

    name: str

    power_kw: float = Field(gt=0)

    power_factor: float = Field(gt=0, le=1)


class LoadFlowAnalysisRequest(BaseModel):

    loads: list[LoadItem]

    source_capacity_kva: float = Field(gt=0)

    voltage_v: float = Field(gt=0)

    phase: str = "three"
