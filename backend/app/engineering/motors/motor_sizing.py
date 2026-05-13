def calculate_motor_full_load_current(
    motor_power_kw: float,
    voltage_v: float,
    power_factor: float,
    efficiency: float
):

    current = (
        motor_power_kw * 1000
    ) / (
        1.732
        * voltage_v
        * power_factor
        * efficiency
    )

    return round(
        current,
        2
    )
