from sqlalchemy import Column, Float, Integer, String, Text, UniqueConstraint

from app.database import Base


class CorrectionFactor(Base):

    __tablename__ = "correction_factors"

    __table_args__ = (
        UniqueConstraint(
            "standard",
            "factor_type",
            "reference_value",
            name="uq_correction_factor"
        ),
    )

    id = Column(Integer, primary_key=True, index=True)

    standard = Column(String(50), default="IEC")

    factor_type = Column(String(100), nullable=False)

    reference_value = Column(Float, nullable=False)

    factor = Column(Float, nullable=False)

    unit = Column(String(50), nullable=True)

    application_context = Column(String(150), nullable=True)

    material = Column(String(50), nullable=True)

    insulation = Column(String(50), nullable=True)

    installation_method = Column(String(50), nullable=True)

    description = Column(Text, nullable=True)

    source_document = Column(String(255), nullable=True)