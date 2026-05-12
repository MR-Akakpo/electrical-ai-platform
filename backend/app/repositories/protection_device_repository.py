from sqlalchemy.orm import Session

from app.models.protection_device_model import ProtectionDevice


def get_protection_devices(db: Session):

    return db.query(
        ProtectionDevice
    ).order_by(
        ProtectionDevice.rated_current_a
    ).all()


def get_breakers_by_current(
    db: Session,
    minimum_current: float
):

    return db.query(
        ProtectionDevice
    ).filter(
        ProtectionDevice.rated_current_a >= minimum_current
    ).order_by(
        ProtectionDevice.rated_current_a
    ).all()