def evaluate_generator_compatibility(
    generator_kva: float,
    capacitor_bank_kvar: float
):

    ratio = (
        capacitor_bank_kvar
        / generator_kva
    ) * 100

    recommendations = []

    compatible = True

    if ratio >= 20:

        compatible = False

        recommendations.append(
            "Capacitor bank too large relative to generator capacity."
        )

    elif ratio >= 10:

        recommendations.append(
            "Verify generator excitation stability with capacitor bank."
        )

    return {
        "compatible": compatible,
        "ratio_percent": round(ratio, 2),
        "recommendations": recommendations
    }
