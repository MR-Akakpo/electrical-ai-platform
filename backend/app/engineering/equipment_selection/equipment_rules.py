def select_equipment_family(
    application: str,
    load_type: str,
    voltage_level: str,
    current_type: str
):

    application = application.lower()
    load_type = load_type.lower()
    voltage_level = voltage_level.upper()
    current_type = current_type.upper()

    families = []

    if "protection" in application or "feeder" in application:
        families.append("protection")
        families.append("switching")

    if load_type == "motor":
        families.append("motor_control")
        families.append("protection")

    if load_type in ["ups", "data_center", "critical"]:
        families.append("protection")
        families.append("switchboard")
        families.append("surge_protection")
        families.append("power_quality")

    if "compensation" in application or "power_factor" in application:
        families.append("power_quality")
        families.append("capacitor_bank")

    if "rectifier" in application or current_type == "DC":
        families.append("rectifier")
        families.append("protection")

    if voltage_level in ["MV", "HTA", "HV"]:
        families.append("mv_switchgear")

    if "switchboard" in application or "tgbt" in application:
        families.append("switchboard")

    if not families:
        families.append("protection")

    return list(dict.fromkeys(families))


def determine_protection_device_type(
    load_current_a: float,
    voltage_level: str
):

    voltage_level = voltage_level.upper()

    if voltage_level in ["MV", "HTA", "HV"]:
        return "MV protection relay + circuit breaker"

    if load_current_a <= 125:
        return "MCB"

    if load_current_a <= 1600:
        return "MCCB"

    return "ACB"


def determine_switchgear_type(
    voltage_level: str,
    criticality: str
):

    voltage_level = voltage_level.upper()
    criticality = criticality.lower()

    if voltage_level in ["MV", "HTA", "HV"]:
        return "MV switchgear panel"

    if criticality in ["critical", "data_center"]:
        return "Form 3b/4 low voltage switchboard recommended"

    return "Standard low voltage switchboard"


def generate_equipment_recommendations(
    application: str,
    load_type: str,
    load_current_a: float,
    voltage_level: str,
    current_type: str,
    short_circuit_level_ka: float,
    criticality: str
):

    recommendations = []

    protection_type = determine_protection_device_type(
        load_current_a=load_current_a,
        voltage_level=voltage_level
    )

    switchgear_type = determine_switchgear_type(
        voltage_level=voltage_level,
        criticality=criticality
    )

    recommendations.append(
        f"Recommended protection device type: {protection_type}."
    )

    recommendations.append(
        f"Recommended switchgear approach: {switchgear_type}."
    )

    if short_circuit_level_ka >= 50:
        recommendations.append(
            "High short-circuit level detected. Verify Icu/Ics, busbar withstand and switchboard short-time rating."
        )

    if current_type.upper() == "DC":
        recommendations.append(
            "DC application detected. Verify DC breaking capacity and arc interruption capability."
        )

    if load_type.lower() == "motor":
        recommendations.append(
            "Motor load detected. Include contactor, overload relay or motor protection circuit breaker, and starting method verification."
        )

    if load_type.lower() in ["ups", "data_center", "critical"]:
        recommendations.append(
            "Critical load detected. Verify selectivity, redundancy, SPD, monitoring and maintenance bypass strategy."
        )

    if "compensation" in application.lower():
        recommendations.append(
            "Reactive compensation detected. Verify detuned reactors and harmonic resonance risk."
        )

    return recommendations
