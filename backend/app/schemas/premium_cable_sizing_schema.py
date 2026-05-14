from pydantic import BaseModel, Field


class PremiumCableSizingRequest(BaseModel):

    power_kw: float = Field(gt=0)

    voltage_v: float = Field(gt=0)

    power_factor: float = Field(default=0.9, gt=0, le=1)

    system_type: str = "three_phase"

    current_type: str = "AC"

    conductor_material: str = "copper"

    insulation_type: str = "xlpe"

    installation_method: str = "cable_tray"

    ambient_temperature_c: float = 30

    grouped_circuits: int = Field(default=1, gt=0)

    cable_length_m: float = Field(gt=0)

    max_voltage_drop_percent: float = Field(default=5, gt=0)

    fault_current_ka: float = Field(default=10, ge=0)

    fault_duration_s: float = Field(default=1, gt=0)

    earthing_system: str = "TN-S"

    load_type: str = "standard"

    thdi_percent: float = Field(default=0, ge=0)

    future_margin_percent: float = Field(default=20, ge=0)

    efficiency: float = Field(default=1, gt=0, le=1)

    parallel_cables: int = Field(default=1, gt=0)
