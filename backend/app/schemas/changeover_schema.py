from pydantic import BaseModel, Field


class ChangeoverAnalysisRequest(BaseModel):

    application: str = "ATS"

    source_1_type: str = "utility"

    source_2_type: str = "generator"

    rated_current_a: float = Field(gt=0)

    load_type: str = "critical"

    criticality: str = "critical"

    transfer_time_s: float = Field(ge=0)

    closed_transition: bool = False
