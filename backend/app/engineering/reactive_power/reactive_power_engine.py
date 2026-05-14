import math


def calculate_reactive_power_compensation(
    active_power_kw: float,
    initial_power_factor: float,
    target_power_factor: float
):

    initial_angle = math.acos(initial_power_factor)

    target_angle = math.acos(target_power_factor)

    kvar_required = (
        active_power_kw
        * (
            math.tan(initial_angle)
            - math.tan(target_angle)
        )
    )

    return round(kvar_required, 2)


def evaluate_power_factor(
    power_factor: float
):

    recommendations = []

    status = "acceptable"

    if power_factor < 0.8:

        status = "poor"

        recommendations.append(
            "Poor power factor detected. Compensation strongly recommended."
        )

    elif power_factor < 0.92:

        status = "moderate"

        recommendations.append(
            "Moderate power factor detected. Compensation may improve efficiency."
        )

    else:

        recommendations.append(
            "Power factor appears acceptable."
        )

    return {
        "status": status,
        "recommendations": recommendations
    }


def recommend_compensation_type(
    kvar_required: float,
    has_harmonics: bool,
    load_variation: str
):

    recommendations = []

    load_variation = load_variation.lower()

    if load_variation == "stable":

        recommendations.append(
            "Fixed capacitor bank may be suitable."
        )

    else:

        recommendations.append(
            "Automatic capacitor bank recommended due to varying load."
        )

    if has_harmonics:

        recommendations.append(
            "Harmonics detected. Detuned or filtered capacitor bank recommended."
        )

    if kvar_required > 300:

        recommendations.append(
            "Large compensation level detected. Multi-step bank recommended."
        )

    return recommendations


def evaluate_resonance_risk(
    has_harmonics: bool,
    capacitor_bank_present: bool
):

    recommendations = []

    risk = "low"

    if has_harmonics and capacitor_bank_present:

        risk = "high"

        recommendations.append(
            "Potential resonance risk detected between harmonics and capacitor bank."
        )

        recommendations.append(
            "Detuned reactors recommended."
        )

    else:

        recommendations.append(
            "No major resonance concern detected."
        )

    return {
        "risk": risk,
        "recommendations": recommendations
    }


def run_reactive_power_analysis(
    active_power_kw: float,
    initial_power_factor: float,
    target_power_factor: float,
    has_harmonics: bool,
    load_variation: str
):

    kvar_required = calculate_reactive_power_compensation(
        active_power_kw=active_power_kw,
        initial_power_factor=initial_power_factor,
        target_power_factor=target_power_factor
    )

    pf_analysis = evaluate_power_factor(
        power_factor=initial_power_factor
    )

    compensation = recommend_compensation_type(
        kvar_required=kvar_required,
        has_harmonics=has_harmonics,
        load_variation=load_variation
    )

    resonance = evaluate_resonance_risk(
        has_harmonics=has_harmonics,
        capacitor_bank_present=True
    )

    recommendations = []

    recommendations.extend(
        pf_analysis["recommendations"]
    )

    recommendations.extend(
        compensation
    )

    recommendations.extend(
        resonance["recommendations"]
    )

    recommendations.append(
        "Verify capacitor switching transients and protection coordination."
    )

    return {
        "required_compensation_kvar": kvar_required,
        "power_factor_analysis": pf_analysis,
        "resonance_analysis": resonance,
        "recommendations": recommendations
    }
