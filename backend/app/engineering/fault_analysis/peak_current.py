def calculate_peak_fault_current(
    symmetrical_fault_current_a: float,
    xr_ratio: float
):

    peak_factor = 1.8

    if xr_ratio >= 14:

        peak_factor = 2.5

    elif xr_ratio >= 7:

        peak_factor = 2.2

    peak_current = (
        symmetrical_fault_current_a
        * peak_factor
    )

    return {
        "peak_factor": peak_factor,
        "peak_current_a": round(
            peak_current,
            2
        )
    }
