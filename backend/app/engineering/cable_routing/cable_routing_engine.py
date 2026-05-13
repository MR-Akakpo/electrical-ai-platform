def calculate_tray_fill_percent(
    total_cable_area_mm2: float,
    tray_width_mm: float,
    tray_height_mm: float
):

    tray_area = tray_width_mm * tray_height_mm

    fill_percent = (
        total_cable_area_mm2
        / tray_area
    ) * 100

    return round(fill_percent, 2)


def evaluate_tray_fill(
    fill_percent: float
):

    recommendations = []

    status = "acceptable"

    if fill_percent > 60:

        status = "critical"

        recommendations.append(
            "Cable tray fill is very high. Increase tray size or split cable routes."
        )

    elif fill_percent > 40:

        status = "high"

        recommendations.append(
            "Cable tray fill is high. Verify ventilation, future expansion and installation practices."
        )

    else:

        recommendations.append(
            "Cable tray fill appears acceptable."
        )

    return {
        "status": status,
        "recommendations": recommendations
    }


def evaluate_cable_separation(
    has_power_cables: bool,
    has_control_cables: bool,
    has_communication_cables: bool,
    has_vfd_cables: bool
):

    recommendations = []

    if has_power_cables and has_communication_cables:

        recommendations.append(
            "Separate power cables from communication cables to reduce electromagnetic interference."
        )

    if has_vfd_cables:

        recommendations.append(
            "VFD cables detected. Use shielded cables and maintain separation from control/communication circuits."
        )

    if has_control_cables and has_power_cables:

        recommendations.append(
            "Control cables should be routed separately from high-current power cables where possible."
        )

    if not recommendations:

        recommendations.append(
            "Cable separation constraints appear acceptable."
        )

    return recommendations


def evaluate_routing_environment(
    environment: str,
    fire_safety_required: bool,
    outdoor: bool
):

    recommendations = []

    environment = environment.lower()

    if outdoor:

        recommendations.append(
            "Outdoor routing detected. Use UV-resistant cable trays and corrosion-resistant materials."
        )

    if environment in ["industrial", "chemical", "marine"]:

        recommendations.append(
            "Harsh environment detected. Verify tray corrosion resistance and cable sheath compatibility."
        )

    if fire_safety_required:

        recommendations.append(
            "Fire safety required. Consider fire-resistant cable routing, fire barriers and LSZH cables."
        )

    return recommendations


def run_cable_routing_analysis(
    total_cable_area_mm2: float,
    tray_width_mm: float,
    tray_height_mm: float,
    has_power_cables: bool,
    has_control_cables: bool,
    has_communication_cables: bool,
    has_vfd_cables: bool,
    environment: str,
    fire_safety_required: bool,
    outdoor: bool
):

    fill_percent = calculate_tray_fill_percent(
        total_cable_area_mm2=total_cable_area_mm2,
        tray_width_mm=tray_width_mm,
        tray_height_mm=tray_height_mm
    )

    fill_analysis = evaluate_tray_fill(
        fill_percent=fill_percent
    )

    separation = evaluate_cable_separation(
        has_power_cables=has_power_cables,
        has_control_cables=has_control_cables,
        has_communication_cables=has_communication_cables,
        has_vfd_cables=has_vfd_cables
    )

    environment_analysis = evaluate_routing_environment(
        environment=environment,
        fire_safety_required=fire_safety_required,
        outdoor=outdoor
    )

    recommendations = []

    recommendations.extend(fill_analysis["recommendations"])
    recommendations.extend(separation)
    recommendations.extend(environment_analysis)

    return {
        "tray_fill_percent": fill_percent,
        "tray_fill_analysis": fill_analysis,
        "separation_recommendations": separation,
        "environment_recommendations": environment_analysis,
        "recommendations": recommendations
    }
