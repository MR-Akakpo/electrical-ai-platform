import math


def calculate_required_kvar(
    active_power_kw: float,
    initial_power_factor: float,
    target_power_factor: float
):

    phi1 = math.acos(
        initial_power_factor
    )

    phi2 = math.acos(
        target_power_factor
    )

    kvar = (
        active_power_kw
        * (
            math.tan(phi1)
            - math.tan(phi2)
        )
    )

    return round(
        kvar,
        2
    )
