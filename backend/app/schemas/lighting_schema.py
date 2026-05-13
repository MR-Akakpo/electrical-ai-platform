from pydantic import BaseModel, Field


class LightingAnalysisRequest(BaseModel):

    area_m2: float = Field(gt=0)

    target_lux: float = Field(gt=0)

    luminaire_efficiency_lm_w: float = Field(gt=0)

    maintenance_factor: float = Field(default=0.8, gt=0, le=1)

    utilization_factor: float = Field(default=0.6, gt=0, le=1)

    emergency_lighting_required: bool = False
