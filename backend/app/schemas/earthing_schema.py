from pydantic import BaseModel, Field


class EarthingAnalysisRequest(BaseModel):

    earth_resistance_ohm: float = Field(gt=0)

    earthing_system: str = "TN-S"

    installation_type: str = "industrial"

    fault_current_a: float = Field(gt=0)

    lightning_protection_required: bool = False
