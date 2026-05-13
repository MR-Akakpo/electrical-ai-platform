def evaluate_harmonic_severity(
    thdi_percent: float,
    thdv_percent: float
):

    severity = "low"

    recommendations = []

    if thdi_percent >= 35 or thdv_percent >= 8:

        severity = "critical"

        recommendations.append(
            "Critical harmonic distortion detected."
        )

    elif thdi_percent >= 20 or thdv_percent >= 5:

        severity = "high"

        recommendations.append(
            "High harmonic distortion detected."
        )

    elif thdi_percent >= 10 or thdv_percent >= 3:

        severity = "moderate"

        recommendations.append(
            "Moderate harmonic distortion detected."
        )

    else:

        recommendations.append(
            "Harmonic distortion appears within a typical acceptable range."
        )

    return {
        "severity": severity,
        "recommendations": recommendations
    }


def evaluate_neutral_overloading(
    single_phase_nonlinear_load_ratio_percent: float
):

    recommendations = []

    overloaded = False

    if single_phase_nonlinear_load_ratio_percent >= 50:

        overloaded = True

        recommendations.append(
            "High nonlinear single-phase load ratio detected. Neutral conductor overloading risk exists."
        )

        recommendations.append(
            "Consider oversized neutral conductor or harmonic mitigation."
        )

    return {
        "neutral_overload_risk": overloaded,
        "recommendations": recommendations
    }


def evaluate_transformer_derating(
    harmonic_k_factor: float
):

    recommendations = []

    if harmonic_k_factor >= 13:

        recommendations.append(
            "High K-factor detected. K-rated transformer recommended."
        )

    elif harmonic_k_factor >= 4:

        recommendations.append(
            "Verify transformer thermal derating under harmonic loading."
        )

    else:

        recommendations.append(
            "Standard transformer may be acceptable depending on thermal study."
        )

    return recommendations


def recommend_harmonic_mitigation(
    severity: str,
    has_vfd: bool,
    has_ups: bool
):

    recommendations = []

    if severity in ["high", "critical"]:

        recommendations.append(
            "Detailed harmonic study recommended."
        )

        recommendations.append(
            "Consider active harmonic filters."
        )

        recommendations.append(
            "Verify capacitor bank resonance risk."
        )

    if has_vfd:

        recommendations.append(
            "VFD loads detected. Consider line reactors or low-harmonic drives."
        )

    if has_ups:

        recommendations.append(
            "UPS system detected. Verify rectifier harmonic performance."
        )

    recommendations.append(
        "Verify IEEE 519 or project harmonic compliance requirements."
    )

    return recommendations


def run_harmonic_analysis(
    thdi_percent: float,
    thdv_percent: float,
    harmonic_k_factor: float,
    single_phase_nonlinear_load_ratio_percent: float,
    has_vfd: bool,
    has_ups: bool
):

    severity = evaluate_harmonic_severity(
        thdi_percent=thdi_percent,
        thdv_percent=thdv_percent
    )

    neutral = evaluate_neutral_overloading(
        single_phase_nonlinear_load_ratio_percent=single_phase_nonlinear_load_ratio_percent
    )

    transformer = evaluate_transformer_derating(
        harmonic_k_factor=harmonic_k_factor
    )

    mitigation = recommend_harmonic_mitigation(
        severity=severity["severity"],
        has_vfd=has_vfd,
        has_ups=has_ups
    )

    recommendations = []

    recommendations.extend(
        severity["recommendations"]
    )

    recommendations.extend(
        neutral["recommendations"]
    )

    recommendations.extend(
        transformer
    )

    recommendations.extend(
        mitigation
    )

    return {
        "thdi_percent": thdi_percent,
        "thdv_percent": thdv_percent,
        "harmonic_severity": severity["severity"],
        "neutral_overload_risk": neutral["neutral_overload_risk"],
        "recommendations": recommendations
    }
