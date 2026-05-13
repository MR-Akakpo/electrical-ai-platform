def generate_generator_recommendations(
    voltage_dip_percent: float,
    autonomy_hours: float,
    redundancy_type: str
):

    recommendations = []

    if voltage_dip_percent > 25:

        recommendations.append(
            "Increase generator capacity to improve motor starting performance."
        )

    if autonomy_hours < 8:

        recommendations.append(
            "Fuel autonomy below recommended minimum for critical infrastructure."
        )

    if redundancy_type == "none":

        recommendations.append(
            "Consider N+1 redundancy for critical applications."
        )

    return recommendations
