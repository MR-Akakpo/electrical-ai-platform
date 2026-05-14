from fastapi import APIRouter

from app.schemas.transformer_schema import (
    TransformerAnalysisRequest
)

from app.engineering.transformers.transformer_engine import (
    run_transformer_analysis
)


router = APIRouter(
    prefix="/engineering/transformers",
    tags=["Transformers"]
)


@router.post("/analysis")
def transformer_analysis(
    data: TransformerAnalysisRequest
):

    return run_transformer_analysis(
        transformer_power_kva=data.transformer_power_kva,
        primary_voltage_v=data.primary_voltage_v,
        secondary_voltage_v=data.secondary_voltage_v,
        connected_load_kva=data.connected_load_kva,
        power_factor=data.power_factor,
        impedance_percent=data.impedance_percent,
        vector_group=data.vector_group,
        cooling_mode=data.cooling_mode,
        no_load_losses_kw=data.no_load_losses_kw,
        load_losses_kw=data.load_losses_kw,
        parallel_operation_required=data.parallel_operation_required,
        second_transformer_impedance_percent=data.second_transformer_impedance_percent,
        second_vector_group=data.second_vector_group
    )
