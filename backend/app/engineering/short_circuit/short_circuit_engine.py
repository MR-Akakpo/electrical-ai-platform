from app.engineering.short_circuit.formulas import (
    calculate_source_impedance_ohm,
    calculate_transformer_impedance_ohm,
    calculate_symmetrical_short_circuit_current,
    calculate_peak_short_circuit_current
)


def run_short_circuit_study(
    voltage_v: float,
    short_circuit_power_mva: float,
    transformer_power_kva: float,
    transformer_uk_percent: float,
    x_r_ratio: float = 10
):

    source_impedance = (
        calculate_source_impedance_ohm(
            voltage_v=voltage_v,
            short_circuit_power_mva=short_circuit_power_mva
        )
    )

    transformer_impedance = (
        calculate_transformer_impedance_ohm(
            voltage_v=voltage_v,
            transformer_power_kva=transformer_power_kva,
            uk_percent=transformer_uk_percent
        )
    )

    total_impedance = (
        source_impedance
        + transformer_impedance
    )

    ik_a = (
        calculate_symmetrical_short_circuit_current(
            voltage_v=voltage_v,
            total_impedance_ohm=total_impedance
        )
    )

    ik_ka = ik_a / 1000

    ip_ka = (
        calculate_peak_short_circuit_current(
            ik_ka=ik_ka,
            x_r_ratio=x_r_ratio
        )
    )

    thermal_1s_ka = ik_ka

    return {

        "voltage_v":
            voltage_v,

        "source_impedance_ohm":
            round(source_impedance, 6),

        "transformer_impedance_ohm":
            round(transformer_impedance, 6),

        "total_impedance_ohm":
            round(total_impedance, 6),

        "symmetrical_short_circuit_ka":
            round(ik_ka, 2),

        "peak_short_circuit_ka":
            round(ip_ka, 2),

        "thermal_1s_short_circuit_ka":
            round(thermal_1s_ka, 2),

        "x_r_ratio":
            x_r_ratio
    }
