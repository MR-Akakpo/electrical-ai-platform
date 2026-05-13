def evaluate_environment_requirements(
    environment: str,
    load_type: str
):

    recommendations = []

    if environment == "outdoor":

        recommendations.append(
            "UV resistant cable recommended."
        )

    if environment == "underground":

        recommendations.append(
            "Use armored cable suitable for buried installation."
        )

    if environment == "marine":

        recommendations.append(
            "Marine corrosion resistant cable required."
        )

    if environment == "chemical":

        recommendations.append(
            "Chemical resistant sheath recommended."
        )

    if environment == "data_center":

        recommendations.append(
            "LSZH cable strongly recommended for data center environments."
        )

    if load_type == "ups":

        recommendations.append(
            "Neutral conductor oversizing may be required due to harmonics."
        )

    if load_type == "generator":

        recommendations.append(
            "Verify voltage drop during transient generator operation."
        )

    if load_type == "critical":

        recommendations.append(
            "Fire resistant cable recommended for critical loads."
        )

    return recommendations
