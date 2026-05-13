def generate_cable_recommendations(
    voltage_drop_percent: float,
    corrected_ampacity: float,
    current: float,
    breaker_rating_a: float,
    material: str,
    max_voltage_drop_percent: float = 5.0
):

    recommendations = []

    if voltage_drop_percent > max_voltage_drop_percent:
        recommendations.append(
            "Voltage drop exceeds the configured engineering limit. Increase cable section or reduce circuit length."
        )

    elif voltage_drop_percent > 0.75 * max_voltage_drop_percent:
        recommendations.append(
            "Voltage drop is close to the engineering limit. Consider increasing cable section for better voltage quality."
        )

    if material == "aluminum":
        recommendations.append(
            "Aluminum cable selected. Verify lug compatibility, tightening torque, corrosion protection and mechanical constraints."
        )

    ampacity_margin = corrected_ampacity - current

    if ampacity_margin < 0:
        recommendations.append(
            "Corrected ampacity is lower than load current. Cable is thermally overloaded."
        )

    elif corrected_ampacity > 0 and ampacity_margin / corrected_ampacity < 0.10:
        recommendations.append(
            "Low ampacity margin detected. Consider higher cable section for operational reserve."
        )

    if breaker_rating_a > corrected_ampacity:
        recommendations.append(
            "Protection rating exceeds corrected cable ampacity. Select a lower protection rating or increase cable section."
        )

    if not recommendations:
        recommendations.append(
            "Cable sizing appears optimized and compliant for the provided engineering assumptions."
        )

    return recommendations
