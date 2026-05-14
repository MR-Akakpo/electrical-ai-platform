def evaluate_earthing_resistance(
    earth_resistance_ohm: float,
    installation_type: str
):

    installation_type = installation_type.lower()

    recommendations = []

    status = "acceptable"

    limit = 10

    if installation_type == "data_center":
        limit = 1

    elif installation_type == "substation":
        limit = 1

    elif installation_type == "industrial":
        limit = 5

    if earth_resistance_ohm > limit:

        status = "high"

        recommendations.append(
            f"Earth resistance too high for {installation_type} application."
        )

        recommendations.append(
            "Consider additional rods, ground ring or ground grid improvement."
        )

    else:

        recommendations.append(
            "Earth resistance appears acceptable."
        )

    return {
        "status": status,
        "limit_ohm": limit,
        "recommendations": recommendations
    }


def evaluate_earthing_system(
    earthing_system: str
):

    recommendations = []

    earthing_system = earthing_system.upper()

    if earthing_system == "TT":

        recommendations.append(
            "TT system detected. RCD protection is generally required."
        )

    elif earthing_system == "TN-S":

        recommendations.append(
            "TN-S system detected. Separate PE and N conductors maintained."
        )

    elif earthing_system == "TN-C":

        recommendations.append(
            "TN-C system detected. PEN conductor continuity is critical."
        )

    elif earthing_system == "TN-C-S":

        recommendations.append(
            "TN-C-S system detected. Verify PEN separation point and bonding."
        )

    elif earthing_system == "IT":

        recommendations.append(
            "IT system detected. Insulation monitoring device recommended."
        )

    else:

        recommendations.append(
            "Custom earthing system configuration detected."
        )

    return recommendations


def evaluate_touch_voltage_risk(
    fault_current_a: float,
    earth_resistance_ohm: float
):

    touch_voltage = (
        fault_current_a
        * earth_resistance_ohm
    )

    recommendations = []

    risk = "low"

    if touch_voltage > 50:

        risk = "high"

        recommendations.append(
            "Dangerous touch voltage detected."
        )

        recommendations.append(
            "Improve grounding and fault clearing time."
        )

    else:

        recommendations.append(
            "Touch voltage appears acceptable."
        )

    return {
        "touch_voltage_v": round(touch_voltage, 2),
        "risk": risk,
        "recommendations": recommendations
    }


def evaluate_lightning_grounding(
    lightning_protection_required: bool
):

    recommendations = []

    if lightning_protection_required:

        recommendations.append(
            "Lightning protection grounding coordination required."
        )

        recommendations.append(
            "Verify bonding between SPD, LPS and grounding network."
        )

    return recommendations


def run_earthing_analysis(
    earth_resistance_ohm: float,
    earthing_system: str,
    installation_type: str,
    fault_current_a: float,
    lightning_protection_required: bool
):

    resistance = evaluate_earthing_resistance(
        earth_resistance_ohm=earth_resistance_ohm,
        installation_type=installation_type
    )

    system = evaluate_earthing_system(
        earthing_system=earthing_system
    )

    touch = evaluate_touch_voltage_risk(
        fault_current_a=fault_current_a,
        earth_resistance_ohm=earth_resistance_ohm
    )

    lightning = evaluate_lightning_grounding(
        lightning_protection_required=lightning_protection_required
    )

    recommendations = []

    recommendations.extend(
        resistance["recommendations"]
    )

    recommendations.extend(system)

    recommendations.extend(
        touch["recommendations"]
    )

    recommendations.extend(lightning)

    recommendations.append(
        "Verify equipotential bonding and grounding conductor sizing."
    )

    return {
        "earth_resistance_analysis": resistance,
        "touch_voltage_analysis": touch,
        "recommendations": recommendations
    }
