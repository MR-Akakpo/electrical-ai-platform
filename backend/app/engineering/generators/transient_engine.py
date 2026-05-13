def calculate_voltage_dip(
    generator_kva: float,
    motor_start_kva: float
):

    if generator_kva <= 0:

        return 100

    dip = (
        motor_start_kva
        / generator_kva
    ) * 100

    return round(
        dip,
        2
    )


def transient_recovery_analysis(
    voltage_dip_percent: float
):

    if voltage_dip_percent <= 15:

        return "Excellent transient performance"

    if voltage_dip_percent <= 25:

        return "Acceptable transient performance"

    return "Poor transient performance"
