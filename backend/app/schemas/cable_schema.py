from pydantic import BaseModel, Field


class CableSizingRequest(BaseModel):

    power_kw: float = Field(gt=0)

    voltage: float = Field(gt=0)

    power_factor: float = Field(gt=0, le=1)

    phase: str = "three"

    length_m: float = Field(gt=0)

    temperature: int = 30

    grouping_circuits: int = 1

    installation_method: str = "C"

    material: str = "copper"

    insulation: str = "xlpe"

    cable_type: str = "multicore"

    fault_time_s: float = 0.2

    environment: str = "industrial"

    load_type: str = "power"

    fire_class: str = "standard"

    emc_type: str = "unshielded"

    harmonic_content_percent: float = 0
