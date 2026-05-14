from datetime import datetime
from typing import Dict, List


def generate_cover_page(
    project_name: str,
    report_title: str,
    company_name: str | None = None
):

    return {
        "project_name": project_name,
        "report_title": report_title,
        "company_name": company_name,
        "generated_at": datetime.utcnow().isoformat(),
    }


def build_kpi_section(
    kpis: Dict
):

    items = []

    for key, value in kpis.items():

        items.append({
            "label": key,
            "value": value
        })

    return items


def build_recommendation_section(
    recommendations: List[str]
):

    return [
        {
            "recommendation": item
        }
        for item in recommendations
    ]


def build_compliance_section(
    compliance_score: float,
    status: str
):

    return {
        "score": compliance_score,
        "status": status,
    }


def generate_premium_engineering_report(
    payload: Dict
):

    report = {
        "report_metadata": generate_cover_page(
            project_name=payload.get(
                "project_name",
                "Engineering Project"
            ),
            report_title=payload.get(
                "report_title",
                "Engineering Report"
            ),
            company_name=payload.get(
                "company_name"
            ),
        ),

        "branding": {
            "include_logo_1": payload.get(
                "include_logo_1",
                False
            ),
            "include_logo_2": payload.get(
                "include_logo_2",
                False
            ),
        },

        "executive_summary": payload.get(
            "executive_summary",
            ""
        ),

        "technical_sections": payload.get(
            "technical_sections",
            []
        ),

        "kpis": build_kpi_section(
            payload.get(
                "kpis",
                {}
            )
        ),

        "compliance": build_compliance_section(
            payload.get(
                "compliance_score",
                0
            ),
            payload.get(
                "compliance_status",
                "UNKNOWN"
            )
        ),

        "recommendations": build_recommendation_section(
            payload.get(
                "recommendations",
                []
            )
        ),

        "appendices": payload.get(
            "appendices",
            []
        ),
    }

    return report
