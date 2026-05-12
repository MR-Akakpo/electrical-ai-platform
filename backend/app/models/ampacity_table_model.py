from sqlalchemy import Column, Float, Integer, String, Text, UniqueConstraint

from app.database import Base


class AmpacityTable(Base):

    __tablename__ = "ampacity_tables"

    __table_args__ = (
        UniqueConstraint(
            "standard",
            "material",
            "insulation",
            "installation_method",
            "section_mm2",
            "conductor_count",
            "temperature_rating",
            name="uq_ampacity_reference"
        ),
    )

    id = Column(Integer, primary_key=True, index=True)

    standard = Column(String(50), nullable=False)

    material = Column(String(50), nullable=False)

    insulation = Column(String(50), nullable=False)

    installation_method = Column(String(50), nullable=False)

    section_mm2 = Column(Float, nullable=False)

    ampacity = Column(Float, nullable=False)

    conductor_count = Column(Integer, default=3)

    temperature_rating = Column(Integer, default=90)

    cable_type = Column(String(50), nullable=True)

    installation_environment = Column(String(100), nullable=True)

    source_document = Column(String(255), nullable=True)

    source_table = Column(String(100), nullable=True)

    notes = Column(Text, nullable=True)