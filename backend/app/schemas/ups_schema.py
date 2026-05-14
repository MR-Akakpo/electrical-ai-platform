from pydantic import BaseModel, Field


class UPSAnalysisRequest(BaseModel):

    ups_power_kva: float = Field(gt=0)

    connected_load_kva: float = Field(gt=0)

    connected_load_kw: float = Field(gt=0)

    battery_voltage_v: float = Field(gt=0)

    battery_capacity_ah: float = Field(gt=0)

    dc_bus_efficiency: float = Field(gt=0, le=1)

    redundancy_type: str = "N+1"

    has_static_bypass: bool = True

    has_maintenance_bypass: bool = True

    application: str = "general"

    battery_type: str = "VRLA"
