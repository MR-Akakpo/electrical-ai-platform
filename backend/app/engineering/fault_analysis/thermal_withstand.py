def calculate_cable_thermal_withstand(
    section_mm2: float,
    k_factor: float,
    fault_duration_s: float
):

    withstand_current = (
        k_factor
        * section_mm2
    ) / (
        fault_duration_s ** 0.5
    )

    return round(
        withstand_current,
        2
    )
