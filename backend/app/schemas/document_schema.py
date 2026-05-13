from pydantic import BaseModel


class DocumentMetadataResponse(BaseModel):

    id: int
    file_name: str
    document_type: str | None = None
    manufacturer: str | None = None
    standard: str | None = None
    source_path: str
    extracted_text_path: str | None = None
    embedding_status: str | None = None
    description: str | None = None

    class Config:
        from_attributes = True
