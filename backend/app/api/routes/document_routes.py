from fastapi import APIRouter

from app.documents.parsers.pdf_parser import (
    extract_pdf_text
)


router = APIRouter(
    prefix="/documents",
    tags=["Engineering Documents"]
)


@router.post("/parse-pdf")
def parse_pdf(
    source_path: str
):

    text = extract_pdf_text(
        source_path
    )

    return {

        "characters": len(text),

        "preview": text[:2000]
    }
