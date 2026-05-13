from pydantic import BaseModel, Field


class SolarBESSAnalysisRequest(BaseModel):

    module_power_wp: float = Field(gt=0)

    number_of_modules: int = Field(gt=0)

    inverter_ac_power_kw: float = Field(gt=0)

    battery_capacity_kwh: float = Field(gt=0)

    critical_load_kw: float = Field(gt=0)

    performance_ratio: float = Field(default=0.8, gt=0, le=1)

    depth_of_discharge: float = Field(default=0.8, gt=0, le=1)
