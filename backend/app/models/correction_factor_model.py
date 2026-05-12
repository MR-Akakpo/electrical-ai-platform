from sqlalchemy import Column

from sqlalchemy import Float

from sqlalchemy import Integer

from sqlalchemy import String

from app.database import Base


class CorrectionFactor(Base):

    __tablename__ = "correction_factors"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    factor_type = Column(
        String,
        nullable=False
    )

    reference_value = Column(
        Float,
        nullable=False
    )

    factor = Column(
        Float,
        nullable=False
    )

    standard = Column(
        String,
        default="IEC"
    )

    description = Column(
        String,
        nullable=True
    )