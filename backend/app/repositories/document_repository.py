from sqlalchemy.orm import Session

from app.models.document_metadata_model import DocumentMetadata


def create_document_metadata(
    db: Session,
    file_name: str,
    source_path: str,
    document_type: str | None = None,
    manufacturer: str | None = None,
    standard: str | None = None,
    description: str | None = None
):

    document = DocumentMetadata(
        file_name=file_name,
        source_path=source_path,
        document_type=document_type,
        manufacturer=manufacturer,
        standard=standard,
        description=description
    )

    db.add(document)
    db.commit()
    db.refresh(document)

    return document


def get_documents(db: Session):

    return db.query(
        DocumentMetadata
    ).order_by(
        DocumentMetadata.created_at.desc()
    ).all()
