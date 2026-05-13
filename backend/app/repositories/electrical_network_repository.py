from sqlalchemy.orm import Session

from app.models.electrical_network_model import (
    ElectricalNetwork
)


def create_network(
    db: Session,
    data
):

    network = ElectricalNetwork(
        **data.model_dump()
    )

    db.add(network)
    db.commit()
    db.refresh(network)

    return network


def get_networks(
    db: Session
):

    return db.query(
        ElectricalNetwork
    ).order_by(
        ElectricalNetwork.id.desc()
    ).all()


def get_network_by_id(
    db: Session,
    network_id: int
):

    return db.query(
        ElectricalNetwork
    ).filter(
        ElectricalNetwork.id == network_id
    ).first()
