def analyze_network_characteristics(
    current_type: str,
    phase_system: str,
    nominal_voltage_v: float,
    earthing_system: str | None,
    source_type: str | None,
    is_critical: bool,
    harmonic_distortion_percent: float | None
):

    recommendations = []

    if current_type == "DC":

        recommendations.append(
            "DC network detected. Verify polarity, DC breaking capacity, insulation coordination and arc interruption capability."
        )

    if phase_system == "single_phase":

        recommendations.append(
            "Single-phase network detected. Verify neutral loading and voltage drop carefully."
        )

    if phase_system == "three_phase":

        recommendations.append(
            "Three-phase network detected. Verify phase balance and neutral current where nonlinear loads exist."
        )

    if earthing_system in ["IT", "isolated"]:

        recommendations.append(
            "IT or isolated earthing detected. Insulation monitoring device should be considered."
        )

    if source_type in ["generator", "ups", "battery", "pv"]:

        recommendations.append(
            "Non-utility source detected. Verify short-circuit contribution and protection coordination."
        )

    if is_critical:

        recommendations.append(
            "Critical network detected. Consider redundancy, selectivity, monitoring and enhanced reliability requirements."
        )

    if harmonic_distortion_percent and harmonic_distortion_percent >= 15:

        recommendations.append(
            "High harmonic distortion detected. Consider neutral oversizing, derating and harmonic filtering."
        )

    if nominal_voltage_v > 1000:

        recommendations.append(
            "Medium/high voltage network detected. Apply dedicated MV/HV protection, insulation and safety studies."
        )

    return {
        "network_classification": {
            "current_type": current_type,
            "phase_system": phase_system,
            "voltage_level": (
                "LV" if nominal_voltage_v <= 1000 else "MV/HV"
            ),
            "source_type": source_type,
            "earthing_system": earthing_system,
            "critical": is_critical
        },
        "recommendations": recommendations
    }
