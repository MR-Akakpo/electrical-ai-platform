from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.schemas.cable_schema import CableSizingRequest
from app.services.calculations.cables.sizing import (
    calculate_current,
    calculate_apparent_power,
    optimize_cable_section
)


router = APIRouter(
    tags=["Cable Sizing"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.post("/cable-sizing")
def cable_sizing(
    data: CableSizingRequest,
    db: Session = Depends(get_db)
):

    current = calculate_current(
        power_kw=data.power_kw,
        voltage=data.voltage,
        power_factor=data.power_factor,
        phase=data.phase
    )

    apparent_power_kva = calculate_apparent_power(
        power_kw=data.power_kw,
        power_factor=data.power_factor
    )

    optimized_cable = optimize_cable_section(
        db=db,
        current=current,
        voltage=data.voltage,
        power_factor=data.power_factor,
        phase=data.phase,
        length_m=data.length_m,
        temperature=data.temperature,
        grouping_circuits=data.grouping_circuits,
        installation_method=data.installation_method,
        material=data.material,
        insulation=data.insulation,
        cable_type=data.cable_type,
        fault_time_s=data.fault_time_s
    )

    return {
        "current": current,
        "apparent_power_kva": apparent_power_kva,
        "optimized_cable": optimized_cable
    }
