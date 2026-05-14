from pydantic import BaseModel, Field


class SLDAnalysisRequest(BaseModel):

    utility_voltage_v: float = Field(gt=0)

    transformer_power_kva: float = Field(gt=0)

    generator_power_kva: float = Field(gt=0)

    ups_power_kva: float = Field(gt=0)

    main_switchboard_power_kva: float = Field(gt=0)
