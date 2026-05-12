from sqlalchemy import Column

from sqlalchemy import Float

from sqlalchemy import Integer

from sqlalchemy import String

from app.database import Base


class AmpacityTable(Base):

    __tablename__ = "ampacity_tables"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    standard = Column(
        String,
        nullable=False
    )

    material = Column(
        String,
        nullable=False
    )

    insulation = Column(
        String,
        nullable=False
    )

    installation_method = Column(
        String,
        nullable=False
    )

    section_mm2 = Column(
        Float,
        nullable=False
    )

    ampacity = Column(
        Float,
        nullable=False
    )

    conductor_count = Column(
        Integer,
        default=3
    )

    temperature_rating = Column(
        Integer,
        default=90
    )