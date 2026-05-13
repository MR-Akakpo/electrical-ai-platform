def determine_capacitor_bank_configuration(
    required_kvar: float
):

    recommendations = []

    stages = []

    if required_kvar <= 25:

        stages = [required_kvar]

    elif required_kvar <= 100:

        stages = [
            required_kvar * 0.25,
            required_kvar * 0.25,
            required_kvar * 0.5
        ]

    else:

        stages = [
            required_kvar * 0.1,
            required_kvar * 0.2,
            required_kvar * 0.2,
            required_kvar * 0.25,
            required_kvar * 0.25
        ]

    stages = [
        round(stage, 2)
        for stage in stages
    ]

    recommendations.append(
        "Automatic power factor correction recommended."
    )

    return {
        "recommended_stages_kvar": stages,
        "recommendations": recommendations
    }
