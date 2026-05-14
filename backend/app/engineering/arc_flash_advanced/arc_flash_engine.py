import math


def estimate_arc_flash_energy(
    voltage_v: float,
    bolted_fault_current_ka: float,
    clearing_time_s: float,
    working_distance_mm: float
):

    energy = (
        4.184
        * (
            voltage_v / 1000
        )
        * bolted_fault_current_ka
        * clearing_time_s
        * (
            610 / working_distance_mm
        ) ** 1.473
    )

    return round(energy, 2)


def determine_ppe_category(
    incident_energy_cal_cm2: float
):

    if incident_energy_cal_cm2 < 1.2:
        return "No arc-rated PPE required"

    if incident_energy_cal_cm2 < 4:
        return "PPE Category 1"

    if incident_energy_cal_cm2 < 8:
        return "PPE Category 2"

    if incident_energy_cal_cm2 < 25:
        return "PPE Category 3"

    if incident_energy_cal_cm2 < 40:
        return "PPE Category 4"

    return "Dangerous - exceeds standard PPE limits"


def evaluate_arc_flash_risk(
    incident_energy_cal_cm2: float
):

    recommendations = []

    risk = "low"

    if incident_energy_cal_cm2 >= 40:

        risk = "extreme"

        recommendations.append(
            "Arc flash energy extremely dangerous."
        )

    elif incident_energy_cal_cm2 >= 25:

        risk = "high"

        recommendations.append(
            "High arc flash hazard detected."
        )

    elif incident_energy_cal_cm2 >= 8:

        risk = "moderate"

        recommendations.append(
            "Moderate arc flash hazard detected."
        )

    else:

        recommendations.append(
            "Arc flash hazard appears limited."
        )

    return {
        "risk": risk,
        "recommendations": recommendations
    }


def recommend_arc_flash_mitigation(
    clearing_time_s: float,
    incident_energy_cal_cm2: float
):

    recommendations = []

    if clearing_time_s > 0.2:

        recommendations.append(
            "Reduce protection clearing time to reduce incident energy."
        )

    if incident_energy_cal_cm2 > 8:

        recommendations.append(
            "Consider arc flash reduction maintenance switch."
        )

        recommendations.append(
            "Remote switching operation recommended."
        )

    recommendations.append(
        "Verify protection coordination and maintenance settings."
    )

    recommendations.append(
        "Install arc flash labels according to NFPA 70E / IEEE 1584."
    )

    return recommendations


def run_arc_flash_analysis(
    voltage_v: float,
    bolted_fault_current_ka: float,
    clearing_time_s: float,
    working_distance_mm: float
):

    incident_energy = estimate_arc_flash_energy(
        voltage_v=voltage_v,
        bolted_fault_current_ka=bolted_fault_current_ka,
        clearing_time_s=clearing_time_s,
        working_distance_mm=working_distance_mm
    )

    ppe = determine_ppe_category(
        incident_energy_cal_cm2=incident_energy
    )

    risk = evaluate_arc_flash_risk(
        incident_energy_cal_cm2=incident_energy
    )

    mitigation = recommend_arc_flash_mitigation(
        clearing_time_s=clearing_time_s,
        incident_energy_cal_cm2=incident_energy
    )

    recommendations = []

    recommendations.extend(
        risk["recommendations"]
    )

    recommendations.extend(
        mitigation
    )

    return {
        "incident_energy_cal_cm2": incident_energy,
        "ppe_category": ppe,
        "risk_analysis": risk,
        "recommendations": recommendations
    }
