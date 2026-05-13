from sqlalchemy import (
    Boolean,
    Column,
    Float,
    Integer,
    String,
    Text
)

from app.database import Base


class ElectricalNetwork(Base):

    __tablename__ = "electrical_networks"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(150), nullable=False)

    description = Column(Text, nullable=True)

    current_type = Column(String(20), nullable=False)

    phase_system = Column(String(50), nullable=False)

    nominal_voltage_v = Column(Float, nullable=False)

    frequency_hz = Column(Float, nullable=True)

    earthing_system = Column(String(50), nullable=True)

    source_type = Column(String(100), nullable=True)

    redundancy_level = Column(String(50), nullable=True)

    is_critical = Column(Boolean, default=False)

    short_circuit_level_ka = Column(Float, nullable=True)

    power_factor = Column(Float, nullable=True)

    harmonic_distortion_percent = Column(Float, nullable=True)

    notes = Column(Text, nullable=True)
