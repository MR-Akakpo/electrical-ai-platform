from pathlib import Path

from app.documents.parsers.pdf_parser import (
    extract_pdf_text
)


def extract_text_basic(
    source_path: str
):

    path = Path(source_path)

    if not path.exists():

        return ""

    suffix = path.suffix.lower()

    if suffix in [".txt", ".md", ".csv"]:

        return path.read_text(
            encoding="utf-8",
            errors="ignore"
        )

    if suffix == ".pdf":

        return extract_pdf_text(
            source_path
        )

    return ""
