from sqlalchemy import Column, DateTime, Integer, String, Text
from sqlalchemy.sql import func

from app.database import Base


class EngineeringStandard(Base):

    __tablename__ = "engineering_standards"

    id = Column(Integer, primary_key=True, index=True)

    code = Column(String(100), nullable=False, unique=True)

    name = Column(String(255), nullable=False)

    domain = Column(String(100), nullable=True)

    country_or_region = Column(String(100), nullable=True)

    version = Column(String(100), nullable=True)

    description = Column(Text, nullable=True)

    source_url = Column(String(255), nullable=True)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )