from pydantic import BaseModel, Field


class ArcFlashAdvancedRequest(BaseModel):

    voltage_v: float = Field(gt=0)

    bolted_fault_current_ka: float = Field(gt=0)

    clearing_time_s: float = Field(gt=0)

    working_distance_mm: float = Field(gt=0)
