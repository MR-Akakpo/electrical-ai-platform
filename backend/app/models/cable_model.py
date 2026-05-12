from sqlalchemy import Column, Float, Integer, String, Text

from app.database import Base


class Cable(Base):

    __tablename__ = "cables"

    id = Column(Integer, primary_key=True, index=True)

    standard = Column(String(50), default="IEC")

    manufacturer = Column(String(100), nullable=True)

    reference = Column(String(150), nullable=True)

    material = Column(String(50), nullable=False)

    insulation = Column(String(50), nullable=True)

    cable_type = Column(String(50), nullable=True)

    installation_method = Column(String(50), nullable=False)

    section_mm2 = Column(Float, nullable=False)

    conductor_count = Column(Integer, default=3)

    voltage_rating_v = Column(Float, nullable=True)

    temperature_rating_c = Column(Integer, nullable=True)

    ampacity = Column(Float, nullable=True)

    resistance_ohm_km = Column(Float, nullable=True)

    reactance_ohm_km = Column(Float, nullable=True)

    description = Column(Text, nullable=True)