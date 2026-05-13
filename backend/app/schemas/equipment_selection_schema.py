from pydantic import BaseModel, Field


class EquipmentSelectionRequest(BaseModel):

    application: str

    load_type: str = "standard"

    load_current_a: float = Field(gt=0)

    voltage_level: str = "LV"

    current_type: str = "AC"

    short_circuit_level_ka: float = Field(ge=0)

    criticality: str = "standard"
