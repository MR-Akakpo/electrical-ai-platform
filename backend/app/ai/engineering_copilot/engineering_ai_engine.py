def generate_engineering_ai_recommendations(
    study_type: str,
    payload: dict
):

    recommendations = []

    warnings = []

    optimizations = []

    compliance = []

    study_type = study_type.lower()

    if study_type == "cable_sizing":

        current = payload.get(
            "design_current_a",
            0
        )

        selected = payload.get(
            "selected_cable",
            {}
        )

        voltage_drop = selected.get(
            "voltage_drop_percent",
            0
        )

        section = selected.get(
            "section_mm2",
            0
        )

        thdi = payload.get(
            "thdi_percent",
            0
        )

        ambient = payload.get(
            "ambient_temperature_c",
            30
        )

        grouped = payload.get(
            "grouped_circuits",
            1
        )

        load_type = payload.get(
            "load_type",
            ""
        )

        if voltage_drop >= 4:
            warnings.append(
                "Voltage drop is approaching critical design limits."
            )

            optimizations.append(
                "Consider increasing cable section or reducing cable length."
            )

        if grouped >= 3:
            warnings.append(
                "Grouped circuits detected. Thermal derating significantly impacts ampacity."
            )

        if ambient >= 45:
            warnings.append(
                "High ambient temperature environment detected."
            )

            optimizations.append(
                "Consider ventilation improvement or higher thermal insulation class."
            )

        if thdi >= 15:
            warnings.append(
                "Harmonic distortion may cause conductor overheating."
            )

            recommendations.append(
                "Neutral conductor oversizing should be evaluated."
            )

        if load_type.lower() in [
            "data_center",
            "ups",
            "nonlinear"
        ]:

            recommendations.append(
                "Nonlinear load profile detected."
            )

            recommendations.append(
                "Consider harmonic filtering and EMC-compliant cable routing."
            )

        if section >= 240:

            optimizations.append(
                "Large conductor section detected."
            )

            optimizations.append(
                "Parallel cable optimization may reduce installation complexity."
            )

        if current >= 800:

            recommendations.append(
                "High-current feeder detected."
            )

            recommendations.append(
                "Busbar trunking evaluation may be beneficial."
            )

        compliance.append(
            "Final cable validation must comply with IEC installation tables and local regulations."
        )

        compliance.append(
            "Protection coordination and short-circuit withstand verification remain mandatory."
        )

    elif study_type == "technical_audit":

        score = payload.get(
            "score_percent",
            0
        )

        critical = payload.get(
            "critical_findings_count",
            0
        )

        if critical > 0:

            warnings.append(
                "Critical audit findings detected."
            )

            recommendations.append(
                "Immediate remediation plan is strongly recommended."
            )

        if score < 70:

            warnings.append(
                "Global audit score below recommended engineering threshold."
            )

        optimizations.append(
            "Implement preventive maintenance tracking."
        )

        optimizations.append(
            "Consider thermal inspection and power quality monitoring integration."
        )

        compliance.append(
            "Audit conclusions must be validated by qualified electrical personnel."
        )

    else:

        recommendations.append(
            "AI engineering copilot active."
        )

        recommendations.append(
            "Advanced engineering interpretation available for this module."
        )

    return {
        "study_type": study_type,
        "recommendations": recommendations,
        "warnings": warnings,
        "optimizations": optimizations,
        "compliance": compliance
    }
