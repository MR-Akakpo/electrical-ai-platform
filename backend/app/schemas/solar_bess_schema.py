from pydantic import BaseModel, Field


class SolarBESSAnalysisRequest(BaseModel):

    daily_consumption_kwh: float = Field(gt=0)

    peak_sun_hours: float = Field(gt=0)

    module_power_wp: float = Field(gt=0)

    module_voc_v: float = Field(gt=0)

    module_vmp_v: float = Field(gt=0)

    inverter_ac_power_kw: float = Field(gt=0)

    inverter_max_dc_voltage_v: float = Field(gt=0)

    inverter_mppt_min_v: float = Field(gt=0)

    inverter_mppt_max_v: float = Field(gt=0)

    battery_capacity_kwh: float = Field(gt=0)

    critical_load_kw: float = Field(gt=0)

    autonomy_days: float = Field(default=1, gt=0)

    performance_ratio: float = Field(default=0.8, gt=0, le=1)

    system_losses_percent: float = Field(default=14, ge=0, lt=100)

    depth_of_discharge: float = Field(default=0.8, gt=0, le=1)

    battery_efficiency: float = Field(default=0.9, gt=0, le=1)

    temperature_correction_factor: float = Field(default=1.15, gt=0)

    system_type: str = "hybrid"

    has_generator_backup: bool = False
