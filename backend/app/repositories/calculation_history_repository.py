from sqlalchemy.orm import Session

from app.models.calculation_history_model import (
    CalculationHistory
)


def save_calculation(

    db: Session,

    power_kw: float,

    voltage: float,

    current: float,

    cable_section: float,

    breaker_rating: float,

    material: str,

    installation_method: str,

    voltage_drop_percent: float
):

    history = CalculationHistory(

        power_kw=power_kw,

        voltage=voltage,

        current=current,

        cable_section=cable_section,

        breaker_rating=breaker_rating,

        material=material,

        installation_method=installation_method,

        voltage_drop_percent=voltage_drop_percent
    )

    db.add(history)

    db.commit()

    db.refresh(history)

    return history