from sqlalchemy import (
    Column,
    Integer,
    Float,
    String
)

from app.database import Base


class CalculationHistory(Base):

    __tablename__ = "calculation_history"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    power_kw = Column(
        Float,
        nullable=False
    )

    voltage = Column(
        Float,
        nullable=False
    )

    current = Column(
        Float,
        nullable=False
    )

    cable_section = Column(
        Float,
        nullable=False
    )

    breaker_rating = Column(
        Float,
        nullable=False
    )

    material = Column(
        String,
        nullable=False
    )

    installation_method = Column(
        String,
        nullable=False
    )

    voltage_drop_percent = Column(
        Float,
        nullable=False
    )