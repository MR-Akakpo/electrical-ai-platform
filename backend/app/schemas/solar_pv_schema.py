from pydantic import BaseModel, Field


class SolarPVAnalysisRequest(BaseModel):

    load_power_kw: float = Field(gt=0)

    operating_hours_per_day: float = Field(gt=0)

    peak_sun_hours: float = Field(gt=0)

    system_efficiency: float = Field(gt=0, le=1)

    autonomy_days: float = Field(gt=0)

    battery_voltage_v: float = Field(gt=0)

    depth_of_discharge: float = Field(gt=0, le=1)

    inverter_power_kw: float = Field(gt=0)

    has_generator_backup: bool = False

    has_grid_connection: bool = True

    has_battery_storage: bool = True
