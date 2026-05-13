from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database import SessionLocal

from app.repositories.engineering_standard_repository import (
    get_standards
)

from app.repositories.protection_device_repository import (
    get_protection_devices
)

from app.repositories.load_profile_repository import (
    get_load_profiles
)

from app.schemas.standard_schema import (
    EngineeringStandardResponse
)

from app.schemas.protection_device_schema import (
    ProtectionDeviceResponse
)

from app.schemas.load_profile_schema import (
    LoadProfileResponse
)

from app.schemas.generator_schema import (
    GeneratorAnalysisRequest
)

from app.schemas.transformer_schema import (
    TransformerAnalysisRequest
)

from app.schemas.ups_schema import (
    UPSAnalysisRequest
)

from app.schemas.protection_coordination_schema import (
    ProtectionCoordinationRequest
)

from app.schemas.power_quality_schema import (
    PowerQualityRequest
)

from app.schemas.fault_analysis_schema import (
    FaultAnalysisRequest
)

from app.schemas.equipment_selection_schema import (
    EquipmentSelectionRequest
)

from app.schemas.reactive_power_schema import (
    ReactivePowerRequest
)

from app.schemas.motor_schema import (
    MotorAnalysisRequest
)

from app.schemas.grounding_schema import (
    GroundingAnalysisRequest
)

from app.schemas.lighting_schema import (
    LightingAnalysisRequest
)

from app.schemas.motor_schema import (
    MotorAnalysisRequest
)

from app.schemas.grounding_schema import (
    GroundingAnalysisRequest
)

from app.schemas.lighting_schema import (
    LightingAnalysisRequest
)

from app.engineering.generators.generator_engine import (
    run_generator_engineering_analysis
)

from app.engineering.transformers.transformer_engine import (
    run_transformer_analysis
)

from app.engineering.ups.ups_engine import (
    run_ups_analysis
)

from app.engineering.protection_coordination.coordination_engine import (
    run_protection_coordination_analysis
)

from app.engineering.power_quality.power_quality_engine import (
    run_power_quality_analysis
)

from app.engineering.fault_analysis.fault_engine import (
    run_fault_analysis
)

from app.engineering.equipment_selection.equipment_selection_engine import (
    run_equipment_selection
)

from app.engineering.reactive_power.reactive_power_engine import (
    run_reactive_power_analysis
)

from app.engineering.motors.motor_engine import (
    run_motor_engineering_analysis
)

from app.engineering.grounding.grounding_engine import (
    analyze_earthing_system
)

from app.engineering.lighting.lighting_engine import (
    analyze_lighting_installation
)

from app.engineering.motors.motor_engine import (
    run_motor_engineering_analysis
)

from app.engineering.grounding.grounding_engine import (
    analyze_earthing_system
)

from app.engineering.lighting.lighting_engine import (
    analyze_lighting_installation
)


router = APIRouter(
    prefix="/engineering",
    tags=["Engineering"]
)


def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()


@router.get(
    "/standards",
    response_model=list[
        EngineeringStandardResponse
    ]
)
def standards(
    db: Session = Depends(get_db)
):

    return get_standards(db)


@router.get(
    "/protection-devices",
    response_model=list[
        ProtectionDeviceResponse
    ]
)
def protection_devices(
    db: Session = Depends(get_db)
):

    return get_protection_devices(db)


@router.get(
    "/load-profiles",
    response_model=list[
        LoadProfileResponse
    ]
)
def load_profiles(
    db: Session = Depends(get_db)
):

    return get_load_profiles(db)


@router.post("/generator-analysis")
def generator_analysis(
    data: GeneratorAnalysisRequest
):

    return run_generator_engineering_analysis(
        total_load_kw=data.total_load_kw,
        power_factor=data.power_factor,
        motor_start_kva=data.motor_start_kva,
        fuel_tank_liters=data.fuel_tank_liters,
        fuel_consumption_lph=data.fuel_consumption_lph,
        load_type=data.load_type,
        redundancy_type=data.redundancy_type
    )


@router.post("/transformer-analysis")
def transformer_analysis(
    data: TransformerAnalysisRequest
):

    return run_transformer_analysis(
        transformer_kva=data.transformer_kva,
        primary_voltage_v=data.primary_voltage_v,
        secondary_voltage_v=data.secondary_voltage_v,
        impedance_percent=data.impedance_percent,
        connected_load_kw=data.connected_load_kw,
        power_factor=data.power_factor,
        phase=data.phase
    )


@router.post("/ups-analysis")
def ups_analysis(
    data: UPSAnalysisRequest
):

    return run_ups_analysis(
        critical_load_kw=data.critical_load_kw,
        power_factor=data.power_factor,
        battery_energy_kwh=data.battery_energy_kwh,
        redundancy_topology=data.redundancy_topology,
        redundancy_factor=data.redundancy_factor
    )


@router.post("/protection-coordination")
def protection_coordination(
    data: ProtectionCoordinationRequest
):

    return run_protection_coordination_analysis(
        upstream_breaker_a=data.upstream_breaker_a,
        downstream_breaker_a=data.downstream_breaker_a,
        upstream_icu_ka=data.upstream_icu_ka,
        downstream_fault_ka=data.downstream_fault_ka,
        breaker_curve=data.breaker_curve,
        load_inrush_multiple=data.load_inrush_multiple
    )


@router.post("/power-quality")
def power_quality_analysis(
    data: PowerQualityRequest
):

    return run_power_quality_analysis(
        thdi_percent=data.thdi_percent,
        thdv_percent=data.thdv_percent,
        nonlinear_load_ratio_percent=data.nonlinear_load_ratio_percent,
        ambient_temperature_c=data.ambient_temperature_c
    )


@router.post("/fault-analysis")
def fault_analysis(
    data: FaultAnalysisRequest
):

    return run_fault_analysis(
        transformer_kva=data.transformer_kva,
        transformer_voltage_v=data.transformer_voltage_v,
        transformer_impedance_percent=data.transformer_impedance_percent,
        generator_kva=data.generator_kva,
        generator_voltage_v=data.generator_voltage_v,
        generator_xdpp_percent=data.generator_xdpp_percent,
        xr_ratio=data.xr_ratio,
        cable_section_mm2=data.cable_section_mm2,
        cable_k_factor=data.cable_k_factor,
        fault_duration_s=data.fault_duration_s
    )


@router.post("/equipment-selection")
def equipment_selection(
    data: EquipmentSelectionRequest
):

    return run_equipment_selection(
        application=data.application,
        load_type=data.load_type,
        load_current_a=data.load_current_a,
        voltage_level=data.voltage_level,
        current_type=data.current_type,
        short_circuit_level_ka=data.short_circuit_level_ka,
        criticality=data.criticality
    )


@router.post("/reactive-power-analysis")
def reactive_power_analysis(
    data: ReactivePowerRequest
):

    return run_reactive_power_analysis(
        active_power_kw=data.active_power_kw,
        initial_power_factor=data.initial_power_factor,
        target_power_factor=data.target_power_factor,
        harmonic_environment=data.harmonic_environment,
        generator_present=data.generator_present,
        generator_kva=data.generator_kva,
        thdi_percent=data.thdi_percent
    )


@router.post("/motor-analysis")
def motor_analysis(
    data: MotorAnalysisRequest
):

    return run_motor_engineering_analysis(
        motor_power_kw=data.motor_power_kw,
        voltage_v=data.voltage_v,
        power_factor=data.power_factor,
        efficiency=data.efficiency,
        starting_method=data.starting_method,
        generator_kva=data.generator_kva
    )


@router.post("/motor-analysis")
def motor_analysis(
    data: MotorAnalysisRequest
):

    return run_motor_engineering_analysis(
        motor_power_kw=data.motor_power_kw,
        voltage_v=data.voltage_v,
        power_factor=data.power_factor,
        efficiency=data.efficiency,
        starting_method=data.starting_method,
        generator_kva=data.generator_kva
    )


@router.post("/grounding-analysis")
def grounding_analysis(
    data: GroundingAnalysisRequest
):

    return analyze_earthing_system(
        earthing_system=data.earthing_system,
        fault_current_a=data.fault_current_a,
        earth_resistance_ohm=data.earth_resistance_ohm,
        touch_voltage_limit_v=data.touch_voltage_limit_v
    )


@router.post("/lighting-analysis")
def lighting_analysis(
    data: LightingAnalysisRequest
):

    return analyze_lighting_installation(
        area_m2=data.area_m2,
        target_lux=data.target_lux,
        luminaire_efficiency_lm_w=data.luminaire_efficiency_lm_w,
        maintenance_factor=data.maintenance_factor,
        utilization_factor=data.utilization_factor,
        emergency_lighting_required=data.emergency_lighting_required
    )
