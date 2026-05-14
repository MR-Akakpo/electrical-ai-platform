from fastapi import APIRouter

from app.schemas.protection_selection_schema import (
    ProtectionSelectionRequest
)

from app.engineering.protection_selection.protection_selection_engine import (
    run_protection_selection
)


router = APIRouter(
    prefix="/engineering/protection-selection",
    tags=["Protection Selection"]
)


@router.post("/analysis")
def protection_selection_analysis(
    data: ProtectionSelectionRequest
):

    return run_protection_selection(
        current_a=data.current_a,
        voltage_v=data.voltage_v,
        application=data.application,
        short_circuit_level_ka=data.short_circuit_level_ka,
        earthing_system=data.earthing_system,
        criticality=data.criticality,
        has_lightning_risk=data.has_lightning_risk,
        incoming_overhead_line=data.incoming_overhead_line
    )
