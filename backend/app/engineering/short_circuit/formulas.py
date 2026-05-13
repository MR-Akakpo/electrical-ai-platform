import math


def calculate_source_impedance_ohm(
    voltage_v: float,
    short_circuit_power_mva: float
):

    return (
        (voltage_v ** 2)
        /
        (short_circuit_power_mva * 1_000_000)
    )


def calculate_transformer_impedance_ohm(
    voltage_v: float,
    transformer_power_kva: float,
    uk_percent: float
):

    base_impedance = (
        (voltage_v ** 2)
        /
        (transformer_power_kva * 1000)
    )

    return (
        base_impedance
        * uk_percent
        / 100
    )


def calculate_symmetrical_short_circuit_current(
    voltage_v: float,
    total_impedance_ohm: float
):

    return (
        voltage_v
        /
        (
            math.sqrt(3)
            * total_impedance_ohm
        )
    )


def calculate_peak_short_circuit_current(
    ik_ka: float,
    x_r_ratio: float = 10
):

    peak_factor = (
        1.02
        + 0.98
        * math.exp(
            -3 / x_r_ratio
        )
    )

    return (
        math.sqrt(2)
        * peak_factor
        * ik_ka
    )
