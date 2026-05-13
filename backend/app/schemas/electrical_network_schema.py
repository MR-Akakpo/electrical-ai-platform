from pydantic import BaseModel, Field


class ElectricalNetworkCreate(BaseModel):

    name: str

    description: str | None = None

    current_type: str = Field(
        default="AC"
    )

    phase_system: str = Field(
        default="three_phase"
    )

    nominal_voltage_v: float = Field(gt=0)

    frequency_hz: float | None = 50

    earthing_system: str | None = "TN-S"

    source_type: str | None = "utility"

    redundancy_level: str | None = None

    is_critical: bool = False

    short_circuit_level_ka: float | None = None

    power_factor: float | None = None

    harmonic_distortion_percent: float | None = None

    notes: str | None = None


class ElectricalNetworkResponse(ElectricalNetworkCreate):

    id: int

    class Config:

        from_attributes = True
