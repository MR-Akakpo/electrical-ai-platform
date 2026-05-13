from app.engineering.fault_analysis.transformer_fault import (
    calculate_transformer_fault_current
)

from app.engineering.fault_analysis.generator_fault import (
    calculate_generator_fault_current
)

from app.engineering.fault_analysis.peak_current import (
    calculate_peak_fault_current
)

from app.engineering.fault_analysis.thermal_withstand import (
    calculate_cable_thermal_withstand
)


def run_fault_analysis(
    transformer_kva: float,
    transformer_voltage_v: float,
    transformer_impedance_percent: float,
    generator_kva: float,
    generator_voltage_v: float,
    generator_xdpp_percent: float,
    xr_ratio: float,
    cable_section_mm2: float,
    cable_k_factor: float,
    fault_duration_s: float
):

    transformer_fault = (
        calculate_transformer_fault_current(
            transformer_kva=transformer_kva,
            voltage_v=transformer_voltage_v,
            impedance_percent=transformer_impedance_percent
        )
    )

    generator_fault = (
        calculate_generator_fault_current(
            generator_kva=generator_kva,
            voltage_v=generator_voltage_v,
            subtransient_reactance_percent=generator_xdpp_percent
        )
    )

    total_fault_current = (
        transformer_fault
        + generator_fault
    )

    peak_current = (
        calculate_peak_fault_current(
            symmetrical_fault_current_a=total_fault_current,
            xr_ratio=xr_ratio
        )
    )

    cable_withstand = (
        calculate_cable_thermal_withstand(
            section_mm2=cable_section_mm2,
            k_factor=cable_k_factor,
            fault_duration_s=fault_duration_s
        )
    )

    recommendations = []

    if total_fault_current > cable_withstand:

        recommendations.append(
            "Cable thermal withstand may be insufficient for the calculated fault current."
        )

    if peak_current["peak_current_a"] > total_fault_current * 2.3:

        recommendations.append(
            "High peak asymmetrical current detected. Verify electrodynamic withstand."
        )

    return {

        "transformer_fault_current_a":
            transformer_fault,

        "generator_fault_current_a":
            generator_fault,

        "total_symmetrical_fault_current_a":
            round(total_fault_current, 2),

        "peak_fault_analysis":
            peak_current,

        "cable_thermal_withstand_a":
            cable_withstand,

        "recommendations":
            recommendations
    }
