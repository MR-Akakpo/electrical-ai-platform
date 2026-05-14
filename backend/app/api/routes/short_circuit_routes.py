from fastapi import APIRouter

from app.schemas.short_circuit_schema import (
    ShortCircuitAnalysisRequest
)

from app.engineering.short_circuit.short_circuit_engine import (
    run_short_circuit_analysis
)


router = APIRouter(
    prefix="/engineering/short-circuit",
    tags=["Short Circuit Calculations"]
)


@router.post("/analysis")
def short_circuit_analysis(
    data: ShortCircuitAnalysisRequest
):

    return run_short_circuit_analysis(
        transformer_power_kva=data.transformer_power_kva,
        voltage_v=data.voltage_v,
        impedance_percent=data.impedance_percent,
        xr_ratio=data.xr_ratio,
        breaker_capacity_ka=data.breaker_capacity_ka,
        fault_duration_s=data.fault_duration_s
    )
