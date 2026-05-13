from pathlib import Path

import pdfplumber
from pypdf import PdfReader


def extract_pdf_text_pypdf(
    source_path: str
):

    text = ""

    try:

        reader = PdfReader(source_path)

        for page in reader.pages:

            extracted = page.extract_text()

            if extracted:

                text += extracted + "\n"

    except Exception as error:

        text += f"\nPYPDF_ERROR: {error}"

    return text


def extract_pdf_text_pdfplumber(
    source_path: str
):

    text = ""

    try:

        with pdfplumber.open(source_path) as pdf:

            for page in pdf.pages:

                extracted = page.extract_text()

                if extracted:

                    text += extracted + "\n"

    except Exception as error:

        text += f"\nPDFPLUMBER_ERROR: {error}"

    return text


def extract_pdf_text(
    source_path: str
):

    path = Path(source_path)

    if not path.exists():

        return ""

    text = extract_pdf_text_pdfplumber(
        source_path
    )

    if len(text.strip()) < 100:

        text = extract_pdf_text_pypdf(
            source_path
        )

    return text
