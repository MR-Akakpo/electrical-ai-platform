def evaluate_selectivity(
    upstream_trip_time_s: float,
    downstream_trip_time_s: float
):

    margin = (
        upstream_trip_time_s
        - downstream_trip_time_s
    )

    recommendations = []

    selective = margin >= 0.1

    if selective:

        recommendations.append(
            "Time selectivity appears acceptable."
        )

    else:

        recommendations.append(
            "Insufficient selectivity margin detected."
        )

        recommendations.append(
            "Adjust protection curves or settings."
        )

    return {
        "selective": selective,
        "time_margin_s": round(margin, 3),
        "recommendations": recommendations
    }


def evaluate_current_discrimination(
    upstream_current_a: float,
    downstream_current_a: float
):

    ratio = (
        upstream_current_a
        / downstream_current_a
    )

    recommendations = []

    if ratio >= 1.5:

        recommendations.append(
            "Current discrimination appears acceptable."
        )

        status = "acceptable"

    else:

        recommendations.append(
            "Current discrimination may be insufficient."
        )

        status = "limited"

    return {
        "status": status,
        "current_ratio": round(ratio, 2),
        "recommendations": recommendations
    }


def evaluate_cascading(
    upstream_breaking_capacity_ka: float,
    prospective_fault_current_ka: float
):

    recommendations = []

    if upstream_breaking_capacity_ka >= prospective_fault_current_ka:

        recommendations.append(
            "Breaking capacity appears acceptable without cascading."
        )

        cascading_required = False

    else:

        cascading_required = True

        recommendations.append(
            "Cascading/back-up protection may be required."
        )

        recommendations.append(
            "Verify manufacturer cascading tables."
        )

    return {
        "cascading_required": cascading_required,
        "recommendations": recommendations
    }


def recommend_critical_installation_strategy(
    installation_type: str
):

    recommendations = []

    installation_type = installation_type.lower()

    if installation_type == "data_center":

        recommendations.append(
            "Data center detected. Total selectivity strongly recommended."
        )

        recommendations.append(
            "Verify UPS downstream discrimination."
        )

    elif installation_type == "hospital":

        recommendations.append(
            "Hospital installation detected. High continuity of service required."
        )

    elif installation_type == "industrial":

        recommendations.append(
            "Industrial installation detected. Verify motor feeder coordination."
        )

    return recommendations


def run_protection_coordination_advanced_analysis(
    upstream_trip_time_s: float,
    downstream_trip_time_s: float,
    upstream_current_a: float,
    downstream_current_a: float,
    upstream_breaking_capacity_ka: float,
    prospective_fault_current_ka: float,
    installation_type: str
):

    selectivity = evaluate_selectivity(
        upstream_trip_time_s=upstream_trip_time_s,
        downstream_trip_time_s=downstream_trip_time_s
    )

    discrimination = evaluate_current_discrimination(
        upstream_current_a=upstream_current_a,
        downstream_current_a=downstream_current_a
    )

    cascading = evaluate_cascading(
        upstream_breaking_capacity_ka=upstream_breaking_capacity_ka,
        prospective_fault_current_ka=prospective_fault_current_ka
    )

    strategy = recommend_critical_installation_strategy(
        installation_type=installation_type
    )

    recommendations = []

    recommendations.extend(
        selectivity["recommendations"]
    )

    recommendations.extend(
        discrimination["recommendations"]
    )

    recommendations.extend(
        cascading["recommendations"]
    )

    recommendations.extend(
        strategy
    )

    recommendations.append(
        "Verify manufacturer selectivity tables."
    )

    recommendations.append(
        "Verify thermal and magnetic protection coordination."
    )

    return {
        "selectivity_analysis": selectivity,
        "discrimination_analysis": discrimination,
        "cascading_analysis": cascading,
        "recommendations": recommendations
    }
