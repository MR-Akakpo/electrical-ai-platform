from app.reporting.premium_report_engine import (
    generate_premium_engineering_report
)

from app.engineering.ai.ai_recommendation_engine import (
    generate_engineering_ai_recommendations
)

from app.engineering.audit.intelligent_audit_engine import (
    run_intelligent_electrical_audit
)


def build_unified_engineering_workflow(
    payload: dict
):

    workflow_type = payload.get(
        "workflow_type",
        "general_engineering"
    )

    recommendations = []

    ai_summary = ""

    compliance_score = 100

    compliance_status = "EXCELLENT"

    audit_result = None


    if workflow_type == "intelligent_audit":

        audit_result = run_intelligent_electrical_audit(
            payload.get(
                "audit_payload",
                {}
            )
        )

        compliance_score = audit_result[
            "compliance_score"
        ]

        compliance_status = audit_result[
            "status"
        ]

        recommendations.extend(
            audit_result[
                "recommendations"
            ]
        )


    ai_data = generate_engineering_ai_recommendations(
        {
            "workflow_type": workflow_type,
            "compliance_score": compliance_score,
            "recommendations": recommendations,
        }
    )

    ai_summary = ai_data.get(
        "executive_summary",
        ""
    )


    report_payload = {
        "project_name": payload.get(
            "project_name",
            "Electrical Engineering Project"
        ),

        "report_title": payload.get(
            "report_title",
            "Engineering Technical Report"
        ),

        "company_name": payload.get(
            "company_name"
        ),

        "include_logo_1": payload.get(
            "include_logo_1",
            False
        ),

        "include_logo_2": payload.get(
            "include_logo_2",
            False
        ),

        "executive_summary": ai_summary,

        "technical_sections": payload.get(
            "technical_sections",
            []
        ),

        "kpis": payload.get(
            "kpis",
            {}
        ),

        "compliance_score": compliance_score,

        "compliance_status": compliance_status,

        "recommendations": recommendations,

        "appendices": payload.get(
            "appendices",
            []
        ),
    }

    report = generate_premium_engineering_report(
        report_payload
    )

    return {
        "workflow_type": workflow_type,
        "audit_result": audit_result,
        "ai_result": ai_data,
        "report": report,
    }
