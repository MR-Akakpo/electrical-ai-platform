from pydantic import BaseModel, Field


class TransformerAnalysisRequest(BaseModel):

    transformer_power_kva: float = Field(gt=0)

    primary_voltage_v: float = Field(gt=0)

    secondary_voltage_v: float = Field(gt=0)

    connected_load_kva: float = Field(gt=0)

    power_factor: float = Field(gt=0, le=1)

    impedance_percent: float = Field(gt=0)

    vector_group: str = "Dyn11"

    cooling_mode: str = "ONAN"

    no_load_losses_kw: float = Field(ge=0)

    load_losses_kw: float = Field(ge=0)

    parallel_operation_required: bool = False

    second_transformer_impedance_percent: float = 6

    second_vector_group: str = "Dyn11"
