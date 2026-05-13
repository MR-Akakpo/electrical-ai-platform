from sqlalchemy import Column, DateTime, Integer, String, Text
from sqlalchemy.sql import func

from app.database import Base


class DocumentMetadata(Base):

    __tablename__ = "document_metadata"

    id = Column(Integer, primary_key=True, index=True)

    file_name = Column(String(255), nullable=False)

    document_type = Column(String(100), nullable=True)

    manufacturer = Column(String(100), nullable=True)

    standard = Column(String(100), nullable=True)

    source_path = Column(String(500), nullable=False)

    extracted_text_path = Column(String(500), nullable=True)

    embedding_status = Column(String(50), default="pending")

    description = Column(Text, nullable=True)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )
