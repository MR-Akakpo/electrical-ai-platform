def generate_engineering_report(
    project_name: str,
    study_type: str,
    title: str,
    input_data: dict,
    result_data: dict,
    recommendations: list[str],
    standard: str = "IEC"
):

    return {
        "project_name": project_name,
        "study_type": study_type,
        "title": title,
        "standard": standard,
        "sections": {
            "input_data": input_data,
            "results": result_data,
            "recommendations": recommendations,
            "engineering_note": (
                "This report is generated from deterministic engineering engines. "
                "Final validation must be performed by a qualified electrical engineer."
            )
        }
    }
