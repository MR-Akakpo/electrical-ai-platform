from pydantic import BaseModel, Field
from typing import Optional


class CableThermalValidationRequest(BaseModel):
    selected_section_mm2: float = Field(gt=0)
    short_circuit_current_ka: float = Field(gt=0)
    fault_duration_s: float = Field(gt=0)
    conductor_material: str
    insulation_type: Optional[str] = None
    conductor_arrangement: str = "phase_or_pe_core_in_multicore_cable"
