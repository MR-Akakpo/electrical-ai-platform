def determine_protection_family(
    current_a: float,
    voltage_v: float,
    application: str,
    short_circuit_level_ka: float
):

    application = application.lower()

    if voltage_v >= 1000:

        return "MV Protection Device"

    if "motor" in application:

        if current_a <= 32:
            return "Motor Protection Circuit Breaker"

        return "MCCB + Thermal Relay"

    if "lighting" in application:

        return "MCB"

    if current_a <= 125:

        return "MCB"

    if current_a <= 1600:

        return "MCCB"

    return "ACB"


def determine_breaking_capacity(
    short_circuit_level_ka: float
):

    if short_circuit_level_ka <= 6:
        return 6

    if short_circuit_level_ka <= 10:
        return 10

    if short_circuit_level_ka <= 16:
        return 16

    if short_circuit_level_ka <= 25:
        return 25

    if short_circuit_level_ka <= 36:
        return 36

    if short_circuit_level_ka <= 50:
        return 50

    return 65


def recommend_rcd(
    earthing_system: str,
    application: str,
    criticality: str
):

    recommendations = []

    earthing_system = earthing_system.upper()
    application = application.lower()
    criticality = criticality.lower()

    if earthing_system in ["TT", "TN-S", "TN-C-S"]:

        recommendations.append(
            "RCD protection should be evaluated according to local regulations and protection philosophy."
        )

    if "socket" in application:

        recommendations.append(
            "30mA RCD likely required for personnel protection."
        )

    if criticality == "critical":

        recommendations.append(
            "For critical installations, verify selective/time-delayed RCD coordination."
        )

    return recommendations


def recommend_spd(
    has_lightning_risk: bool,
    incoming_overhead_line: bool,
    criticality: str
):

    recommendations = []

    if has_lightning_risk or incoming_overhead_line:

        recommendations.append(
            "Type 1 SPD recommended at main incoming switchboard."
        )

    recommendations.append(
        "Type 2 SPD recommended for downstream LV distribution."
    )

    if criticality.lower() == "critical":

        recommendations.append(
            "Critical installation detected. Consider coordinated SPD architecture and sensitive equipment protection."
        )

    return recommendations


def run_protection_selection(
    current_a: float,
    voltage_v: float,
    application: str,
    short_circuit_level_ka: float,
    earthing_system: str,
    criticality: str,
    has_lightning_risk: bool,
    incoming_overhead_line: bool
):

    protection_family = determine_protection_family(
        current_a=current_a,
        voltage_v=voltage_v,
        application=application,
        short_circuit_level_ka=short_circuit_level_ka
    )

    breaking_capacity = determine_breaking_capacity(
        short_circuit_level_ka=short_circuit_level_ka
    )

    rcd = recommend_rcd(
        earthing_system=earthing_system,
        application=application,
        criticality=criticality
    )

    spd = recommend_spd(
        has_lightning_risk=has_lightning_risk,
        incoming_overhead_line=incoming_overhead_line,
        criticality=criticality
    )

    recommendations = []

    recommendations.extend(rcd)
    recommendations.extend(spd)

    recommendations.append(
        "Verify selectivity/discrimination with upstream and downstream protections."
    )

    recommendations.append(
        "Verify manufacturer coordination tables and IEC compliance."
    )

    return {
        "recommended_protection_family": protection_family,
        "recommended_breaking_capacity_ka": breaking_capacity,
        "recommendations": recommendations
    }
