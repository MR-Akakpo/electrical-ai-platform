from pydantic import BaseModel


class ManufacturerCatalogItemResponse(BaseModel):

    id: int
    manufacturer: str
    product_family: str
    product_type: str
    reference: str
    rated_current_a: float | None = None
    rated_voltage_v: float | None = None
    breaking_capacity_ka: float | None = None
    poles: int | None = None
    curve: str | None = None
    standard: str | None = None
    application: str | None = None
    technical_data: dict | None = None
    source_document: str | None = None
    notes: str | None = None

    class Config:
        from_attributes = True
