def audit_project_consistency(
    project_name: str,
    studies: list,
    networks: list | None = None
):

    recommendations = []
    study_types = [study.get("study_type") for study in studies]

    required_studies = [
        "load_flow",
        "short_circuit",
        "cable_sizing",
        "protection_coordination",
        "earthing",
        "power_quality"
    ]

    missing = []

    for item in required_studies:
        if item not in study_types:
            missing.append(item)

    if missing:
        recommendations.append(
            "Missing important engineering studies: " + ", ".join(missing)
        )
    else:
        recommendations.append(
            "Core engineering studies appear available."
        )

    if networks is not None and len(networks) == 0:
        recommendations.append(
            "No electrical network model found. Create network topology before final validation."
        )

    return {
        "project_name": project_name,
        "studies_count": len(studies),
        "available_study_types": study_types,
        "missing_core_studies": missing,
        "recommendations": recommendations
    }
