from sqlalchemy import Column, Float, Integer, String, Text

from app.database import Base


class ProtectionDevice(Base):

    __tablename__ = "protection_devices"

    id = Column(Integer, primary_key=True, index=True)

    standard = Column(String(50), default="IEC")

    manufacturer = Column(String(100), nullable=True)

    reference = Column(String(150), nullable=True)

    device_type = Column(String(100), nullable=False)

    technology = Column(String(100), nullable=True)

    rated_current_a = Column(Float, nullable=False)

    poles = Column(Integer, nullable=True)

    curve = Column(String(50), nullable=True)

    breaking_capacity_ka = Column(Float, nullable=True)

    service_breaking_capacity_ka = Column(Float, nullable=True)

    rated_voltage_v = Column(Float, nullable=True)

    frequency_hz = Column(Float, nullable=True)

    application = Column(String(150), nullable=True)

    description = Column(Text, nullable=True)