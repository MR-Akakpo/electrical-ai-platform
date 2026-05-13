from fastapi import APIRouter

from app.ai.document_analysis.engineering_knowledge_service import (
    knowledge_status,
    scan_engineering_documents,
    process_document
)

from app.ai.vectorstore.vector_store_manager import (
    semantic_search,
    vectorstore_statistics
)

from app.ai.copilot.engineering_copilot import (
    engineering_copilot_preview
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

    return vectorstore_statistics()


@router.get("/semantic-search")
def engineering_semantic_search(
    query: str
):

    return semantic_search(
        query=query
    )


@router.get("/copilot/preview")
def copilot_preview(
    query: str
):

    return engineering_copilot_preview(
        query=query
    )
