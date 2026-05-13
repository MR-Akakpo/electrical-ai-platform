def calculate_transformer_fault_current(
    transformer_kva: float,
    voltage_v: float,
    impedance_percent: float
):

    if impedance_percent <= 0:

        return 0

    full_load_current = (
        transformer_kva * 1000
    ) / (
        1.732 * voltage_v
    )

    fault_current = (
        full_load_current
        * 100
        / impedance_percent
    )

    return round(
        fault_current,
        2
    )
