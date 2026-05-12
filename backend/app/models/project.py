from sqlalchemy import Column, DateTime, Integer, String, Text
from sqlalchemy.sql import func

from app.database import Base


class Project(Base):

    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(150), nullable=False)

    description = Column(Text, nullable=True)

    client_name = Column(String(150), nullable=True)

    site_name = Column(String(150), nullable=True)

    project_type = Column(String(100), nullable=True)

    voltage_level = Column(String(50), nullable=True)

    standard = Column(String(50), default="IEC")

    status = Column(String(50), default="draft")

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )