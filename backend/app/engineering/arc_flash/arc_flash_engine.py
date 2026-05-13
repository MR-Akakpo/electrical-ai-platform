def estimate_arc_flash_risk_level(
    fault_current_ka: float,
    clearing_time_s: float,
    working_distance_mm: float,
    system_voltage_v: float
):

    energy_index = (
        fault_current_ka
        * clearing_time_s
        * system_voltage_v
    ) / working_distance_mm

    risk_level = "low"

    recommendations = []

    if energy_index >= 20:
        risk_level = "critical"
        recommendations.append(
            "Critical arc flash risk detected. Detailed IEEE 1584 / IEC arc flash study required."
        )

    elif energy_index >= 10:
        risk_level = "high"
        recommendations.append(
            "High arc flash risk detected. Review protection clearing time and working procedures."
        )

    elif energy_index >= 5:
        risk_level = "moderate"
        recommendations.append(
            "Moderate arc flash risk detected. Verify PPE category and safe working distance."
        )

    else:
        recommendations.append(
            "Estimated arc flash risk is low, but formal safety verification remains required."
        )

    return {
        "energy_index": round(energy_index, 3),
        "risk_level": risk_level,
        "recommendations": recommendations
    }


def recommend_arc_flash_mitigation(
    risk_level: str
):

    recommendations = []

    if risk_level in ["high", "critical"]:
        recommendations.append(
            "Reduce protective device clearing time where possible."
        )
        recommendations.append(
            "Consider arc flash detection relay or zone selective interlocking."
        )
        recommendations.append(
            "Improve switchboard compartmentalization and remote operation."
        )

    if risk_level == "critical":
        recommendations.append(
            "Restrict live work and perform detailed incident energy calculation."
        )

    recommendations.append(
        "Apply lockout/tagout, labeling, PPE and safe approach boundaries."
    )

    return recommendations


def run_arc_flash_analysis(
    fault_current_ka: float,
    clearing_time_s: float,
    working_distance_mm: float,
    system_voltage_v: float,
    equipment_type: str = "switchboard"
):

    risk = estimate_arc_flash_risk_level(
        fault_current_ka=fault_current_ka,
        clearing_time_s=clearing_time_s,
        working_distance_mm=working_distance_mm,
        system_voltage_v=system_voltage_v
    )

    mitigation = recommend_arc_flash_mitigation(
        risk_level=risk["risk_level"]
    )

    return {
        "equipment_type": equipment_type,
        "fault_current_ka": fault_current_ka,
        "clearing_time_s": clearing_time_s,
        "working_distance_mm": working_distance_mm,
        "system_voltage_v": system_voltage_v,
        "risk_assessment": risk,
        "mitigation_recommendations": mitigation,
        "note": "This is a preliminary screening. Formal arc flash studies require detailed IEEE 1584 / IEC methodology and equipment data."
    }
