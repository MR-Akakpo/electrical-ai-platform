from datetime import datetime
from uuid import uuid4

DOCUMENT_REPOSITORY = []


def register_engineering_document(
    study_type: str,
    title: str,
    project_name: str,
    file_name: str,
    file_path: str,
    generated_by: str = "Engineering Platform",
    version: str = "A",
    status: str = "GENERATED",
):

    document = {
        "document_id": str(uuid4()),
        "study_type": study_type,
        "title": title,
        "project_name": project_name,
        "file_name": file_name,
        "file_path": file_path,
        "generated_by": generated_by,
        "version": version,
        "status": status,
        "generated_at": str(datetime.now()),
    }

    DOCUMENT_REPOSITORY.append(document)

    return document


def list_engineering_documents():

    return {
        "total_documents": len(DOCUMENT_REPOSITORY),
        "documents": DOCUMENT_REPOSITORY[::-1],
    }


def filter_documents_by_study(
    study_type: str
):

    filtered = [
        doc
        for doc in DOCUMENT_REPOSITORY
        if doc["study_type"] == study_type
    ]

    return {
        "study_type": study_type,
        "total_documents": len(filtered),
        "documents": filtered[::-1],
    }
