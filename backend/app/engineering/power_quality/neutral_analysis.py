def analyze_neutral_loading(
    nonlinear_load_ratio_percent: float
):

    oversizing_required = False

    recommendations = []

    if nonlinear_load_ratio_percent >= 40:

        oversizing_required = True

        recommendations.append(
            "Neutral conductor oversizing recommended due to triplen harmonics."
        )

    if nonlinear_load_ratio_percent >= 70:

        recommendations.append(
            "Consider 200% neutral sizing for severe nonlinear load environments."
        )

    return {
        "oversizing_required": oversizing_required,
        "recommendations": recommendations
    }
