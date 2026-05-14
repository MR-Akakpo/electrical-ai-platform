from typing import Dict, List

from app.engineering.doctrine.doctrine_engine import (
    validate_study_documents,
    validate_voltage_drop,
    validate_grounding_system,
    validate_underground_network,
    validate_mv_substation,
)


def run_intelligent_electrical_audit(
    payload: Dict
) -> Dict:

    audit_results = []

    compliance_score = 100

    recommendations = []


    if "study_documents" in payload:

        study_result = validate_study_documents(
            payload["study_documents"]
        )

        audit_results.append({
            "category": "Study Documentation",
            "result": study_result
        })

        if not study_result["compliant"]:

            compliance_score -= 10

            recommendations.append(
                "Complete missing engineering study documents."
            )


    if "voltage_drop" in payload:

        vd = payload["voltage_drop"]

        voltage_result = validate_voltage_drop(
            vd["usage_type"],
            vd["value_percent"]
        )

        audit_results.append({
            "category": "Voltage Drop",
            "result": voltage_result
        })

        if not voltage_result["compliant"]:

            compliance_score -= 10

            recommendations.append(
                "Reduce voltage drop to comply with engineering limits."
            )


    if "grounding" in payload:

        grounding = payload["grounding"]

        grounding_result = validate_grounding_system(
            grounding["installation_type"],
            grounding["measured_resistance_ohm"]
        )

        audit_results.append({
            "category": "Grounding System",
            "result": grounding_result
        })

        if not grounding_result["compliant"]:

            compliance_score -= 15

            recommendations.append(
                "Improve grounding system resistance."
            )


    if "underground_network" in payload:

        underground = payload["underground_network"]

        underground_result = validate_underground_network(
            underground["network_type"],
            underground["burial_depth_m"],
            underground["warning_mesh"],
            underground["sand_bedding"]
        )

        audit_results.append({
            "category": "Underground Network",
            "result": underground_result
        })

        if not underground_result["compliant"]:

            compliance_score -= 15

            recommendations.append(
                "Correct underground cable installation deficiencies."
            )


    if "mv_substation" in payload:

        mv = payload["mv_substation"]

        mv_result = validate_mv_substation(
            mv["has_surge_protection"],
            mv["has_protection_relay"],
            mv["grounding_interlock"]
        )

        audit_results.append({
            "category": "MV Substation",
            "result": mv_result
        })

        if not mv_result["compliant"]:

            compliance_score -= 20

            recommendations.append(
                "Upgrade MV protection and interlocking systems."
            )


    if compliance_score >= 90:
        status = "EXCELLENT"

    elif compliance_score >= 75:
        status = "ACCEPTABLE"

    elif compliance_score >= 50:
        status = "LIMITED COMPLIANCE"

    else:
        status = "NON COMPLIANT"


    return {
        "audit_type": "Intelligent Electrical Engineering Audit",
        "compliance_score": compliance_score,
        "status": status,
        "audit_results": audit_results,
        "recommendations": recommendations,
    }
