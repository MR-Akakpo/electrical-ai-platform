from app.engineering.reactive_power.power_factor_correction import (
    calculate_required_kvar
)

from app.engineering.reactive_power.capacitor_bank_sizing import (
    determine_capacitor_bank_configuration
)

from app.engineering.reactive_power.resonance_analysis import (
    evaluate_resonance_risk
)

from app.engineering.reactive_power.generator_compatibility import (
    evaluate_generator_compatibility
)


def run_reactive_power_analysis(
    active_power_kw: float,
    initial_power_factor: float,
    target_power_factor: float,
    harmonic_environment: bool,
    generator_present: bool,
    generator_kva: float,
    thdi_percent: float
):

    required_kvar = (
        calculate_required_kvar(
            active_power_kw=active_power_kw,
            initial_power_factor=initial_power_factor,
            target_power_factor=target_power_factor
        )
    )

    capacitor_bank = (
        determine_capacitor_bank_configuration(
            required_kvar=required_kvar
        )
    )

    resonance = (
        evaluate_resonance_risk(
            harmonic_environment=harmonic_environment,
            generator_present=generator_present,
            thdi_percent=thdi_percent
        )
    )

    generator_compatibility = (
        evaluate_generator_compatibility(
            generator_kva=generator_kva,
            capacitor_bank_kvar=required_kvar
        )
    )

    recommendations = []

    recommendations.extend(
        capacitor_bank["recommendations"]
    )

    recommendations.extend(
        resonance["recommendations"]
    )

    recommendations.extend(
        generator_compatibility["recommendations"]
    )

    if resonance["risk"] == "high":

        recommendations.append(
            "Use detuned capacitor bank with harmonic filtering."
        )

    return {

        "required_reactive_power_kvar":
            required_kvar,

        "capacitor_bank_configuration":
            capacitor_bank,

        "resonance_analysis":
            resonance,

        "generator_compatibility":
            generator_compatibility,

        "recommendations":
            recommendations
    }
