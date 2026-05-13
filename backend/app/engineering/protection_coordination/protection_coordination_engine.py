def evaluate_selectivity(
    upstream_breaker_rating_a: float,
    downstream_breaker_rating_a: float,
    upstream_trip_time_s: float,
    downstream_trip_time_s: float
):

    selective = True

    recommendations = []

    if upstream_breaker_rating_a <= downstream_breaker_rating_a:

        selective = False

        recommendations.append(
            "Upstream breaker rating should generally exceed downstream breaker rating."
        )

    if upstream_trip_time_s <= downstream_trip_time_s:

        selective = False

        recommendations.append(
            "Upstream breaker trips too fast compared to downstream breaker."
        )

    if selective:

        recommendations.append(
            "Basic time/current selectivity appears acceptable."
        )

    return {
        "selective": selective,
        "recommendations": recommendations
    }


def evaluate_cascading(
    upstream_breaking_capacity_ka: float,
    downstream_fault_level_ka: float
):

    cascading_possible = (
        upstream_breaking_capacity_ka
        >= downstream_fault_level_ka
    )

    recommendations = []

    if cascading_possible:

        recommendations.append(
            "Cascading/back-up protection may be feasible depending on manufacturer coordination tables."
        )

    else:

        recommendations.append(
            "Insufficient upstream breaking capacity for cascading approach."
        )

    return {
        "cascading_possible": cascading_possible,
        "recommendations": recommendations
    }


def evaluate_protection_philosophy(
    application: str,
    criticality: str
):

    recommendations = []

    application = application.lower()
    criticality = criticality.lower()

    if criticality == "critical":

        recommendations.append(
            "Critical installation detected. Full discrimination/selectivity study recommended."
        )

    if "data_center" in application:

        recommendations.append(
            "Data center application detected. Verify UPS bypass coordination and downstream selectivity."
        )

    if "motor" in application:

        recommendations.append(
            "Motor feeder detected. Verify overload and short-circuit coordination."
        )

    if "generator" in application:

        recommendations.append(
            "Generator source detected. Verify protection sensitivity during island operation."
        )

    return recommendations


def run_protection_coordination_analysis(
    upstream_breaker_rating_a: float,
    downstream_breaker_rating_a: float,
    upstream_trip_time_s: float,
    downstream_trip_time_s: float,
    upstream_breaking_capacity_ka: float,
    downstream_fault_level_ka: float,
    application: str,
    criticality: str
):

    selectivity = evaluate_selectivity(
        upstream_breaker_rating_a=upstream_breaker_rating_a,
        downstream_breaker_rating_a=downstream_breaker_rating_a,
        upstream_trip_time_s=upstream_trip_time_s,
        downstream_trip_time_s=downstream_trip_time_s
    )

    cascading = evaluate_cascading(
        upstream_breaking_capacity_ka=upstream_breaking_capacity_ka,
        downstream_fault_level_ka=downstream_fault_level_ka
    )

    philosophy = evaluate_protection_philosophy(
        application=application,
        criticality=criticality
    )

    recommendations = []

    recommendations.extend(
        selectivity["recommendations"]
    )

    recommendations.extend(
        cascading["recommendations"]
    )

    recommendations.extend(
        philosophy
    )

    return {
        "selectivity_analysis": selectivity,
        "cascading_analysis": cascading,
        "recommendations": recommendations
    }
