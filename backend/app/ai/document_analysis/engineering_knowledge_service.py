from pathlib import Path

from app.documents.loaders.document_loader import (
    list_raw_documents
)

from app.documents.parsers.text_extractor import (
    extract_text_basic
)


PROCESSED_DIR = Path(
    "app/knowledge/processed_documents"
)


def scan_engineering_documents():

    return list_raw_documents()


def process_document(
    source_path: str
):

    PROCESSED_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    text = extract_text_basic(
        source_path
    )

    source = Path(source_path)

    output_path = PROCESSED_DIR / f"{source.stem}.txt"

    output_path.write_text(
        text,
        encoding="utf-8"
    )

    return {
        "source_path": source_path,
        "extracted_text_path": str(output_path),
        "characters": len(text)
    }


def knowledge_status():

    documents = scan_engineering_documents()

    return {
        "raw_documents_count": len(documents),
        "raw_documents": documents,
        "status": "document_architecture_ready"
    }
