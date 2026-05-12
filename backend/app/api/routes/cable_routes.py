from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from app.database import (
    SessionLocal
)

from app.schemas.cable_schema import (
    CableSizingRequest
)

from app.services.calculation.cables.sizing import (
    calculate_current,
    calculate_apparent_power,
    installation_method_factor,
    optimize_cable_section
)

router = APIRouter()


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

    method_factor = installation_method_factor(
        data.installation_method
    )

    optimized_cable = optimize_cable_section(

        db=db,

        current=current,

        voltage=data.voltage,

        length_m=data.length_m,

        temperature_factor=data.temperature_factor,

        grouping_factor=data.grouping_factor,

        installation_method=data.installation_method,

        installation_factor=method_factor,

        material=data.material
    )

    return {

        "current": current,

        "apparent_power_kva": apparent_power_kva,

        "installation_method_factor": method_factor,

        "optimized_cable": optimized_cable
    }