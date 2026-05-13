from pydantic import BaseModel, Field


class UPSAnalysisRequest(BaseModel):

    critical_load_kw: float = Field(gt=0)

    power_factor: float = Field(gt=0, le=1)

    battery_energy_kwh: float = Field(gt=0)

    redundancy_topology: str = "N+1"

    redundancy_factor: float = Field(default=1.2, gt=0)
