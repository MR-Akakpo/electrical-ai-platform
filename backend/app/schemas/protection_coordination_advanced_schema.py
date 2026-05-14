from pydantic import BaseModel, Field


class ProtectionCoordinationAdvancedRequest(BaseModel):

    upstream_trip_time_s: float = Field(gt=0)

    downstream_trip_time_s: float = Field(gt=0)

    upstream_current_a: float = Field(gt=0)

    downstream_current_a: float = Field(gt=0)

    upstream_breaking_capacity_ka: float = Field(gt=0)

    prospective_fault_current_ka: float = Field(gt=0)

    installation_type: str = "industrial"
