from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal

from app.schemas.electrical_network_schema import (
    ElectricalNetworkCreate,
    ElectricalNetworkResponse
)

from app.repositories.electrical_network_repository import (
    create_network,
    get_networks,
    get_network_by_id
)

from app.engineering.network.network_engine import (
    analyze_network_characteristics
)


router = APIRouter(
    prefix="/engineering/networks",
    tags=["Electrical Networks"]
)


def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()


@router.post(
    "/",
    response_model=ElectricalNetworkResponse
)
def create_electrical_network(
    data: ElectricalNetworkCreate,
    db: Session = Depends(get_db)
):

    return create_network(
        db=db,
        data=data
    )


@router.get(
    "/",
    response_model=list[ElectricalNetworkResponse]
)
def list_electrical_networks(
    db: Session = Depends(get_db)
):

    return get_networks(db)


@router.get(
    "/{network_id}",
    response_model=ElectricalNetworkResponse
)
def get_electrical_network(
    network_id: int,
    db: Session = Depends(get_db)
):

    network = get_network_by_id(
        db=db,
        network_id=network_id
    )

    if not network:

        raise HTTPException(
            status_code=404,
            detail="Electrical network not found"
        )

    return network


@router.post("/analyze")
def analyze_network(
    data: ElectricalNetworkCreate
):

    return analyze_network_characteristics(
        current_type=data.current_type,
        phase_system=data.phase_system,
        nominal_voltage_v=data.nominal_voltage_v,
        earthing_system=data.earthing_system,
        source_type=data.source_type,
        is_critical=data.is_critical,
        harmonic_distortion_percent=data.harmonic_distortion_percent
    )
