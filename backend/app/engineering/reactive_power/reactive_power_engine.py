import math


def calculate_reactive_power_compensation(
    active_power_kw: float,
    initial_power_factor: float,
    target_power_factor: float
):

    initial_angle = math.acos(initial_power_factor)

    target_angle = math.acos(target_power_factor)

    kvar_required = active_power_kw * (
        math.tan(initial_angle) - math.tan(target_angle)
    )

    return round(kvar_required, 2)


def run_reactive_power_analysis(
    active_power_kw: float,
    initial_power_factor: float,
    target_power_factor: float,
    has_harmonics: bool | None = None,
    load_variation: str = "variable",
    harmonic_environment: bool | None = None,
    generator_present: bool = False,
    generator_kva: float = 0,
    thdi_percent: float = 0
):

    if has_harmonics is None:
        has_harmonics = bool(harmonic_environment) or thdi_percent >= 15

    kvar_required = calculate_reactive_power_compensation(
        active_power_kw=active_power_kw,
        initial_power_factor=initial_power_factor,
        target_power_factor=target_power_factor
    )

    recommendations = []

    if initial_power_factor < 0.8:
        recommendations.append("Poor power factor detected. Compensation strongly recommended.")
    elif initial_power_factor < 0.92:
        recommendations.append("Moderate power factor detected. Compensation may improve efficiency.")
    else:
        recommendations.append("Power factor appears acceptable.")

    if load_variation.lower() == "stable":
        recommendations.append("Fixed capacitor bank may be suitable.")
    else:
        recommendations.append("Automatic capacitor bank recommended due to varying load.")

    if has_harmonics:
        recommendations.append("Harmonics detected. Detuned or filtered capacitor bank recommended.")
        recommendations.append("Verify resonance risk with capacitor banks.")

    if generator_present:
        recommendations.append("Generator present. Verify excitation stability and capacitor bank switching impact.")

    if generator_kva > 0:
        ratio = (kvar_required / generator_kva) * 100
        if ratio >= 20:
            recommendations.append("Capacitor bank appears high relative to generator capacity.")

    recommendations.append("Verify capacitor switching transients and protection coordination.")

    return {
        "required_compensation_kvar": kvar_required,
        "initial_power_factor": initial_power_factor,
        "target_power_factor": target_power_factor,
        "has_harmonics": has_harmonics,
        "load_variation": load_variation,
        "generator_present": generator_present,
        "recommendations": recommendations
    }
