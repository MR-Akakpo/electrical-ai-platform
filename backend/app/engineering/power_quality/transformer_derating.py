def calculate_transformer_derating(
    thdi_percent: float
):

    derating_factor = 1.0

    if thdi_percent >= 40:

        derating_factor = 0.7

    elif thdi_percent >= 25:

        derating_factor = 0.8

    elif thdi_percent >= 15:

        derating_factor = 0.9

    return {
        "derating_factor": derating_factor,
        "recommended_transformer_capacity_multiplier": round(
            1 / derating_factor,
            2
        )
    }
