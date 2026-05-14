from pathlib import Path
import json


EXPORT_DIR = Path("app/exports")


def ensure_export_dir():

    EXPORT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )


def export_report_json(
    file_name: str,
    report_data: dict
):

    ensure_export_dir()

    output_path = EXPORT_DIR / f"{file_name}.json"

    output_path.write_text(
        json.dumps(report_data, indent=4, ensure_ascii=False),
        encoding="utf-8"
    )

    return {
        "format": "json",
        "path": str(output_path),
        "status": "exported"
    }


def export_report_markdown(
    file_name: str,
    report_data: dict
):

    ensure_export_dir()

    output_path = EXPORT_DIR / f"{file_name}.md"

    lines = []

    lines.append(f"# {report_data.get('title', 'Engineering Report')}")
    lines.append("")
    lines.append(f"**Project:** {report_data.get('project_name', '')}")
    lines.append(f"**Study Type:** {report_data.get('study_type', '')}")
    lines.append(f"**Standard:** {report_data.get('standard', 'IEC')}")
    lines.append("")
    lines.append("## Input Data")
    lines.append("```json")
    lines.append(json.dumps(report_data.get("input_data", {}), indent=4, ensure_ascii=False))
    lines.append("```")
    lines.append("")
    lines.append("## Results")
    lines.append("```json")
    lines.append(json.dumps(report_data.get("result_data", {}), indent=4, ensure_ascii=False))
    lines.append("```")
    lines.append("")
    lines.append("## Recommendations")

    for recommendation in report_data.get("recommendations", []):
        lines.append(f"- {recommendation}")

    lines.append("")
    lines.append("> Final validation must be performed by a qualified electrical engineer.")

    output_path.write_text(
        "\n".join(lines),
        encoding="utf-8"
    )

    return {
        "format": "markdown",
        "path": str(output_path),
        "status": "exported"
    }


def export_engineering_report(
    file_name: str,
    report_data: dict,
    export_format: str = "json"
):

    safe_name = file_name.replace(" ", "_").replace("/", "_").lower()

    if export_format == "markdown":

        return export_report_markdown(
            file_name=safe_name,
            report_data=report_data
        )

    return export_report_json(
        file_name=safe_name,
        report_data=report_data
    )
