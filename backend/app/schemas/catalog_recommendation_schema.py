from pydantic import BaseModel, Field


class CatalogRecommendationRequest(BaseModel):

    product_type: str = "MCCB"

    load_current_a: float = Field(gt=0)

    manufacturer: str | None = None
