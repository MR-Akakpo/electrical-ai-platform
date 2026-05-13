def evaluate_overheating_risk(
    thdi_percent: float,
    ambient_temperature_c: float
):

    risk = "low"

    recommendations = []

    if thdi_percent >= 30 and ambient_temperature_c >= 35:

        risk = "high"

        recommendations.append(
            "Combined harmonic distortion and high ambient temperature increase overheating risk."
        )

    elif thdi_percent >= 20:

        risk = "moderate"

        recommendations.append(
            "Moderate overheating risk due to harmonic currents."
        )

    return {
        "risk": risk,
        "recommendations": recommendations
    }
