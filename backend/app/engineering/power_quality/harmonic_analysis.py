def evaluate_harmonic_severity(
    thdi_percent: float,
    thdv_percent: float
):

    severity = "normal"

    recommendations = []

    if thdi_percent >= 40:

        severity = "critical"

        recommendations.append(
            "Very high current harmonic distortion detected."
        )

    elif thdi_percent >= 20:

        severity = "high"

        recommendations.append(
            "High current harmonic distortion detected."
        )

    if thdv_percent >= 8:

        recommendations.append(
            "Voltage harmonic distortion exceeds typical IEEE 519 recommendations."
        )

    return {
        "severity": severity,
        "recommendations": recommendations
    }
