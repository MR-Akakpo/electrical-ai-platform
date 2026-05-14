from datetime import datetime
from pathlib import Path
from uuid import uuid4

from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet


EXPORT_DIR = Path("exports")

EXPORT_DIR.mkdir(
    exist_ok=True
)


def build_engineering_pdf_report(
    title: str,
    project_name: str,
    sections: list,
):

    file_name = f"{uuid4()}.pdf"

    output_path = EXPORT_DIR / file_name

    document = SimpleDocTemplate(
        str(output_path),
        pagesize=A4,
    )

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph(
            title,
            styles["Title"]
        )
    )

    elements.append(
        Spacer(1, 20)
    )

    elements.append(
        Paragraph(
            f"<b>Project:</b> {project_name}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"<b>Generated:</b> {datetime.now()}",
            styles["BodyText"]
        )
    )

    elements.append(
        Spacer(1, 20)
    )

    for section in sections:

        elements.append(
            Paragraph(
                section["title"],
                styles["Heading2"]
            )
        )

        elements.append(
            Spacer(1, 10)
        )

        elements.append(
            Paragraph(
                section["content"],
                styles["BodyText"]
            )
        )

        elements.append(
            Spacer(1, 15)
        )

        if section.get("table"):

            table = Table(
                section["table"]
            )

            table.setStyle(
                TableStyle([
                    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#0f172a")),
                    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                    ("GRID", (0, 0), (-1, -1), 1, colors.black),
                    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                    ("BOTTOMPADDING", (0, 0), (-1, 0), 10),
                ])
            )

            elements.append(table)

            elements.append(
                Spacer(1, 20)
            )

    document.build(elements)

    return {
        "status": "success",
        "file_name": file_name,
        "file_path": str(output_path),
    }
