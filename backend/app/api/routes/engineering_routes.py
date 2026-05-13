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

from app.engineering.generators.generator_engine import (
    run_generator_engineering_analysis
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
