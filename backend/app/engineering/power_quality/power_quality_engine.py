from app.engineering.power_quality.harmonic_analysis import (
    evaluate_harmonic_severity
)

from app.engineering.power_quality.neutral_analysis import (
    analyze_neutral_loading
)

from app.engineering.power_quality.transformer_derating import (
    calculate_transformer_derating
)

from app.engineering.power_quality.overheating_risk import (
    evaluate_overheating_risk
)


def run_power_quality_analysis(
    thdi_percent: float,
    thdv_percent: float,
    nonlinear_load_ratio_percent: float,
    ambient_temperature_c: float
):

    harmonic_analysis = evaluate_harmonic_severity(
        thdi_percent=thdi_percent,
        thdv_percent=thdv_percent
    )

    neutral_analysis = analyze_neutral_loading(
        nonlinear_load_ratio_percent=nonlinear_load_ratio_percent
    )

    transformer_derating = calculate_transformer_derating(
        thdi_percent=thdi_percent
    )

    overheating = evaluate_overheating_risk(
        thdi_percent=thdi_percent,
        ambient_temperature_c=ambient_temperature_c
    )

    recommendations = []

    recommendations.extend(
        harmonic_analysis["recommendations"]
    )

    recommendations.extend(
        neutral_analysis["recommendations"]
    )

    recommendations.extend(
        overheating["recommendations"]
    )

    if thdi_percent >= 35:

        recommendations.append(
            "Consider active or passive harmonic filtering."
        )

    return {

        "harmonic_analysis":
            harmonic_analysis,

        "neutral_analysis":
            neutral_analysis,

        "transformer_derating":
            transformer_derating,

        "overheating_risk":
            overheating,

        "recommendations":
            recommendations
    }
