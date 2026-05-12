from sqlalchemy import Column, Float, Integer, String, Text

from app.database import Base


class LoadProfile(Base):

    __tablename__ = "load_profiles"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False, unique=True)

    description = Column(Text, nullable=True)

    typical_power_factor = Column(Float, nullable=True)

    max_voltage_drop_percent = Column(Float, nullable=True)

    demand_factor = Column(Float, nullable=True)

    simultaneity_factor = Column(Float, nullable=True)

    diversity_factor = Column(Float, nullable=True)

    starting_current_factor = Column(Float, nullable=True)

    harmonic_factor = Column(Float, nullable=True)

    reliability_level = Column(String(100), nullable=True)

    source_reference = Column(String(255), nullable=True)