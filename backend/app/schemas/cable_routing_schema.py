from pydantic import BaseModel, Field


class CableRoutingAnalysisRequest(BaseModel):

    total_cable_area_mm2: float = Field(gt=0)

    tray_width_mm: float = Field(gt=0)

    tray_height_mm: float = Field(gt=0)

    has_power_cables: bool = True

    has_control_cables: bool = False

    has_communication_cables: bool = False

    has_vfd_cables: bool = False

    environment: str = "industrial"

    fire_safety_required: bool = False

    outdoor: bool = False
