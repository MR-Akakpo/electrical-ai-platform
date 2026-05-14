from fastapi import APIRouter

from app.schemas.cable_thermal_schema import CableThermalValidationRequest
from app.engineering.cable_thermal.thermal_short_circuit_engine import (
    validate_thermal_withstand,
    calculate_required_thermal_section_mm2,
    calculate_permissible_short_circuit_current_ka,
)

router = APIRouter(
    prefix="/engineering/cable-thermal",
    tags=["Cable Thermal Withstand"],
)


@router.post("/validate")
def validate_cable_thermal_withstand(
    request: CableThermalValidationRequest,
):
    return validate_thermal_withstand(
        selected_section_mm2=request.selected_section_mm2,
        short_circuit_current_ka=request.short_circuit_current_ka,
        fault_duration_s=request.fault_duration_s,
        conductor_material=request.conductor_material,
        insulation_type=request.insulation_type,
        conductor_arrangement=request.conductor_arrangement,
    )


@router.post("/required-section")
def required_thermal_section(
    request: CableThermalValidationRequest,
):
    return calculate_required_thermal_section_mm2(
        short_circuit_current_ka=request.short_circuit_current_ka,
        fault_duration_s=request.fault_duration_s,
        conductor_material=request.conductor_material,
        insulation_type=request.insulation_type,
        conductor_arrangement=request.conductor_arrangement,
    )


@router.post("/permissible-current")
def permissible_short_circuit_current(
    request: CableThermalValidationRequest,
):
    return calculate_permissible_short_circuit_current_ka(
        section_mm2=request.selected_section_mm2,
        fault_duration_s=request.fault_duration_s,
        conductor_material=request.conductor_material,
        insulation_type=request.insulation_type,
        conductor_arrangement=request.conductor_arrangement,
    )
