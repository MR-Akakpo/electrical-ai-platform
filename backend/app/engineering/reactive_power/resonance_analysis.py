def evaluate_resonance_risk(
    harmonic_environment: bool,
    generator_present: bool,
    thdi_percent: float
):

    risk = "low"

    recommendations = []

    if harmonic_environment:

        risk = "moderate"

        recommendations.append(
            "Harmonic environment detected."
        )

    if thdi_percent >= 20:

        risk = "high"

        recommendations.append(
            "High harmonic distortion detected. Detuned reactor strongly recommended."
        )

    if generator_present:

        recommendations.append(
            "Generator operation may increase resonance sensitivity."
        )

    return {
        "risk": risk,
        "recommendations": recommendations
    }
