def recommend_motor_cable_strategy(
    motor_power_kw: float,
    starting_method: str
):

    recommendations = []

    if motor_power_kw >= 75:

        recommendations.append(
            "Consider armored XLPE motor feeder cable."
        )

    if starting_method.lower() == "vfd":

        recommendations.append(
            "Use shielded VFD-rated cable to reduce EMC issues."
        )

    recommendations.append(
        "Verify voltage drop during motor starting."
    )

    return recommendations
