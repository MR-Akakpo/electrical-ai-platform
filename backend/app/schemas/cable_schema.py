from pydantic import BaseModel


class CableSizingRequest(BaseModel):

    power_kw: float

    voltage: float

    power_factor: float

    phase: str

    length_m: float

    temperature_factor: float

    grouping_factor: float

    installation_method: str

    material: str