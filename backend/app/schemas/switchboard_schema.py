from pydantic import BaseModel, Field


class SwitchboardAnalysisRequest(BaseModel):

    application: str = "TGBT"

    rated_current_a: float = Field(gt=0)

    short_circuit_level_ka: float = Field(ge=0)

    duration_s: float = Field(default=1, gt=0)

    environment: str = "indoor"

    criticality: str = "standard"

    maintenance_requirement: str = "medium"
