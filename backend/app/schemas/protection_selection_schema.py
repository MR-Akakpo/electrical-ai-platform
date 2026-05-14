from pydantic import BaseModel, Field


class ProtectionSelectionRequest(BaseModel):

    current_a: float = Field(gt=0)

    voltage_v: float = Field(gt=0)

    application: str = "general"

    short_circuit_level_ka: float = Field(ge=0)

    earthing_system: str = "TN-S"

    criticality: str = "standard"

    has_lightning_risk: bool = False

    incoming_overhead_line: bool = False
