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
