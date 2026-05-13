from pydantic import BaseModel, Field


class ProtectionCoordinationRequest(BaseModel):

    upstream_breaker_rating_a: float = Field(gt=0)

    downstream_breaker_rating_a: float = Field(gt=0)

    upstream_trip_time_s: float = Field(gt=0)

    downstream_trip_time_s: float = Field(gt=0)

    upstream_breaking_capacity_ka: float = Field(gt=0)

    downstream_fault_level_ka: float = Field(gt=0)

    application: str = "general"

    criticality: str = "standard"
