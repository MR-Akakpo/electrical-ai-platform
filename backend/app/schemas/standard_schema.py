from pydantic import BaseModel


class EngineeringStandardResponse(BaseModel):

    id: int
    code: str
    name: str
    domain: str | None = None
    country_or_region: str | None = None
    version: str | None = None
    description: str | None = None
    source_url: str | None = None

    class Config:
        from_attributes = True