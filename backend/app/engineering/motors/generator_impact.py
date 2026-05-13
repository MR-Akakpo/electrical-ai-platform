def evaluate_generator_motor_impact(
    generator_kva: float,
    motor_starting_kva: float
):

    ratio = (
        motor_starting_kva
        / generator_kva
    ) * 100

    recommendations = []

    acceptable = True

    if ratio >= 50:

        acceptable = False

        recommendations.append(
            "Motor starting impact on generator is very high."
        )

    elif ratio >= 30:

        recommendations.append(
            "Verify generator transient voltage dip during motor starting."
        )

    return {
        "acceptable": acceptable,
        "impact_ratio_percent": round(
            ratio,
            2
        ),
        "recommendations": recommendations
    }
