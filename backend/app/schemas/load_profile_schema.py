from pydantic import BaseModel


class LoadProfileResponse(BaseModel):

    id: int
    name: str
    description: str | None = None
    typical_power_factor: float | None = None
    max_voltage_drop_percent: float | None = None
    demand_factor: float | None = None
    simultaneity_factor: float | None = None
    diversity_factor: float | None = None
    starting_current_factor: float | None = None
    harmonic_factor: float | None = None
    reliability_level: str | None = None
    source_reference: str | None = None

    class Config:
        from_attributes = True