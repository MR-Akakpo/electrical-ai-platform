def recommend_motor_protection(
    motor_current_a: float,
    starting_method: str
):

    recommendations = []

    breaker_type = "MPCB"

    if motor_current_a >= 100:

        breaker_type = "MCCB + protection relay"

    recommendations.append(
        f"Recommended motor protection: {breaker_type}."
    )

    recommendations.append(
        "Thermal overload protection recommended."
    )

    if starting_method.lower() == "vfd":

        recommendations.append(
            "Include VFD input/output protection and harmonic mitigation."
        )

    return recommendations
