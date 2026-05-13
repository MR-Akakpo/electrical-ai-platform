from app.engineering.protection_coordination.coordination_rules import (
    evaluate_selectivity,
    evaluate_backup_protection
)

from app.engineering.protection_coordination.trip_curve_engine import (
    analyze_trip_curve
)


def run_protection_coordination_analysis(
    upstream_breaker_a: float,
    downstream_breaker_a: float,
    upstream_icu_ka: float,
    downstream_fault_ka: float,
    breaker_curve: str,
    load_inrush_multiple: float
):

    selectivity = evaluate_selectivity(
        upstream_breaker_a=upstream_breaker_a,
        downstream_breaker_a=downstream_breaker_a
    )

    backup = evaluate_backup_protection(
        upstream_icu_ka=upstream_icu_ka,
        downstream_fault_ka=downstream_fault_ka
    )

    trip_curve = analyze_trip_curve(
        breaker_curve=breaker_curve,
        inrush_multiple=load_inrush_multiple
    )

    recommendations = []

    if selectivity["selective"] is False:

        recommendations.append(
            "Increase upstream/downstream protection discrimination ratio."
        )

    if backup["backup_protection"] is False:

        recommendations.append(
            "Increase upstream breaker breaking capacity."
        )

    if trip_curve["compatible"] is False:

        recommendations.append(
            "Use a more suitable breaker curve for motor or transformer energization."
        )

    return {

        "selectivity":
            selectivity,

        "backup_protection":
            backup,

        "trip_curve_analysis":
            trip_curve,

        "recommendations":
            recommendations
    }
