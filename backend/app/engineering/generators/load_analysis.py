def calculate_generator_required_capacity(
    total_load_kw: float,
    power_factor: float,
    future_expansion_percent: float = 20
):

    kva = (
        total_load_kw
        / power_factor
    )

    kva *= (
        1
        + future_expansion_percent / 100
    )

    return round(
        kva,
        2
    )


def evaluate_load_type(
    load_type: str
):

    if load_type == "motor":

        return {
            "oversizing_factor":
                1.5,

            "notes":
                "Motor starting impact must be considered."
        }

    if load_type == "ups":

        return {
            "oversizing_factor":
                1.3,

            "notes":
                "UPS rectifier harmonics and transient response must be considered."
        }

    if load_type == "nonlinear":

        return {
            "oversizing_factor":
                1.4,

            "notes":
                "Harmonic-producing loads detected."
        }

    return {

        "oversizing_factor":
            1.1,

        "notes":
            "Standard load profile."
    }
