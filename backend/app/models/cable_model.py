from sqlalchemy import (
    Column,
    Integer,
    Float,
    String
)

from app.database import Base


class Cable(Base):

    __tablename__ = "cables"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    section_mm2 = Column(
        Float,
        nullable=False
    )

    ampacity = Column(
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