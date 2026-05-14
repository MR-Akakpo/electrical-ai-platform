from sqlalchemy import Column, Integer, String, Text, JSON
from app.database import Base


class EngineeringStudy(Base):

    __tablename__ = "engineering_studies"

    id = Column(Integer, primary_key=True, index=True)

    project_name = Column(String(255), nullable=False)

    study_type = Column(String(100), nullable=False)

    title = Column(String(255), nullable=False)

    description = Column(Text, nullable=True)

    input_data = Column(JSON, nullable=True)

    result_data = Column(JSON, nullable=True)

    engineering_standard = Column(String(100), nullable=True)

    status = Column(String(50), default="draft")
