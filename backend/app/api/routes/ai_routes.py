from fastapi import APIRouter

from app.ai.document_analysis.engineering_knowledge_service import (
    knowledge_status,
    scan_engineering_documents,
    process_document
)

from app.ai.vectorstore.vector_store_manager import (
    vectorstore_status
)


router = APIRouter(
    prefix="/ai",
    tags=["AI Engineering"]
)


@router.get("/knowledge/status")
def get_knowledge_status():

    return knowledge_status()


@router.get("/documents/scan")
def scan_documents():

    return scan_engineering_documents()


@router.post("/documents/process")
def process_engineering_document(
    source_path: str
):

    return process_document(
        source_path=source_path
    )


@router.get("/vectorstore/status")
def get_vectorstore_status():

    return vectorstore_status()
