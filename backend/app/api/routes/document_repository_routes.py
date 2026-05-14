from fastapi import APIRouter

from app.document_repository.document_repository_engine import (
    list_engineering_documents,
    filter_documents_by_study,
)

router = APIRouter(
    prefix="/engineering-documents",
    tags=["Engineering Document Repository"],
)


@router.get("/")
def engineering_documents():
    return list_engineering_documents()


@router.get("/study/{study_type}")
def documents_by_study(
    study_type: str
):
    return filter_documents_by_study(
        study_type
    )
