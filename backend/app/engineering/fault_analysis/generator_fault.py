def calculate_generator_fault_current(
    generator_kva: float,
    voltage_v: float,
    subtransient_reactance_percent: float
):

    if subtransient_reactance_percent <= 0:

        return 0

    full_load_current = (
        generator_kva * 1000
    ) / (
        1.732 * voltage_v
    )

    fault_current = (
        full_load_current
        * 100
        / subtransient_reactance_percent
    )

    return round(
        fault_current,
        2
    )
