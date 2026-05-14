from sqlalchemy import Column, Float, Integer, String, Text, JSON
from app.database import Base


class ManufacturerCatalogItem(Base):

    __tablename__ = "manufacturer_catalog_items"

    id = Column(Integer, primary_key=True, index=True)

    manufacturer = Column(String(100), nullable=False)

    product_family = Column(String(100), nullable=False)

    product_type = Column(String(100), nullable=False)

    reference = Column(String(150), nullable=False)

    rated_current_a = Column(Float, nullable=True)

    rated_voltage_v = Column(Float, nullable=True)

    breaking_capacity_ka = Column(Float, nullable=True)

    poles = Column(Integer, nullable=True)

    curve = Column(String(50), nullable=True)

    standard = Column(String(100), nullable=True)

    application = Column(String(150), nullable=True)

    technical_data = Column(JSON, nullable=True)

    source_document = Column(String(255), nullable=True)

    notes = Column(Text, nullable=True)
