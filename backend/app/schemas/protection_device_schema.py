from pydantic import BaseModel


class ProtectionDeviceResponse(BaseModel):

    id: int
    standard: str | None = None
    manufacturer: str | None = None
    reference: str | None = None
    device_type: str
    technology: str | None = None
    rated_current_a: float
    poles: int | None = None
    curve: str | None = None
    breaking_capacity_ka: float | None = None
    service_breaking_capacity_ka: float | None = None
    rated_voltage_v: float | None = None
    frequency_hz: float | None = None
    application: str | None = None
    description: str | None = None

    class Config:
        from_attributes = True