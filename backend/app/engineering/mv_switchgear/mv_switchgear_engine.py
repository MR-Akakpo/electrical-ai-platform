def determine_mv_cubicle_type(
    application: str
):

    application = application.lower()

    if "transformer" in application or "transfo" in application:
        return "Transformer feeder cubicle"

    if "incoming" in application or "arrival" in application or "arrivee" in application:
        return "Incoming MV cubicle"

    if "metering" in application or "comptage" in application:
        return "MV metering cubicle"

    if "motor" in application:
        return "MV motor feeder cubicle"

    if "rmu" in application:
        return "Ring Main Unit"

    return "General MV feeder cubicle"


def recommend_switching_device(
    rated_current_a: float,
    short_circuit_level_ka: float,
    application: str
):

    application = application.lower()

    if short_circuit_level_ka >= 25:
        return "Vacuum Circuit Breaker recommended"

    if "transformer" in application and rated_current_a <= 200:
        return "Switch-fuse combination may be acceptable depending on utility requirements"

    return "Load Break Switch or Vacuum Circuit Breaker depending on protection philosophy"


def recommend_mv_protection(
    application: str,
    earthing_system: str
):

    application = application.lower()
    earthing_system = earthing_system.upper()

    protections = []

    protections.append("Overcurrent protection 50/51")

    if "transformer" in application:
        protections.append("Earth fault protection 50N/51N")
        protections.append("Transformer temperature / Buchholz interface if applicable")

    if "motor" in application:
        protections.append("Motor protection relay")
        protections.append("Thermal image protection")
        protections.append("Locked rotor protection")

    if earthing_system == "IT":
        protections.append("Insulation monitoring / earth fault detection")

    return protections


def run_mv_switchgear_analysis(
    application: str,
    rated_voltage_kv: float,
    rated_current_a: float,
    short_circuit_level_ka: float,
    earthing_system: str,
    indoor: bool = True
):

    cubicle_type = determine_mv_cubicle_type(
        application=application
    )

    switching_device = recommend_switching_device(
        rated_current_a=rated_current_a,
        short_circuit_level_ka=short_circuit_level_ka,
        application=application
    )

    protections = recommend_mv_protection(
        application=application,
        earthing_system=earthing_system
    )

    recommendations = []

    if rated_voltage_kv >= 24:
        recommendations.append(
            "Verify insulation level, BIL, creepage distances and utility requirements."
        )

    if short_circuit_level_ka >= 25:
        recommendations.append(
            "High MV fault level detected. Verify making/breaking capacity and short-time withstand."
        )

    if indoor:
        recommendations.append(
            "Indoor MV switchgear detected. Verify ventilation, arc-flash pressure relief and access clearance."
        )
    else:
        recommendations.append(
            "Outdoor MV switchgear detected. Verify IP rating, corrosion protection and environmental constraints."
        )

    recommendations.append(
        "Coordinate MV protection settings with upstream utility and downstream transformer LV protections."
    )

    return {
        "recommended_cubicle_type": cubicle_type,
        "rated_voltage_kv": rated_voltage_kv,
        "rated_current_a": rated_current_a,
        "short_circuit_level_ka": short_circuit_level_ka,
        "recommended_switching_device": switching_device,
        "recommended_protections": protections,
        "recommendations": recommendations
    }
