from app.engineering.protection.protection_types import (
    PROTECTION_DEVICE_TYPES
)


STANDARD_BREAKERS = [

    2,
    4,
    6,
    10,
    16,
    20,
    25,
    32,
    40,
    50,
    63,
    80,
    100,
    125,
    160,
    200,
    250,
    320,
    400,
    630,
    800,
    1000,
    1250,
    1600,
    2500,
    3200,
    4000,
    6300
]


def determine_device_type(
    breaker_rating: float
):

    if breaker_rating <= 125:
        return "MCB"

    elif breaker_rating <= 1600:
        return "MCCB"

    return "ACB"


def determine_breaking_capacity(
    prospective_short_circuit_ka: float,
    device_type: str
):

    available = PROTECTION_DEVICE_TYPES[
        device_type
    ].get(
        "typical_breaking_capacity_ka",
        []
    )

    for value in available:

        if value >= prospective_short_circuit_ka:
            return value

    if available:
        return max(available)

    return None


def select_protection_device(
    load_current: float,
    corrected_ampacity: float,
    prospective_short_circuit_ka: float = 25,
    safety_margin: float = 1.10,
    future_expansion_factor: float = 1.20
):

    design_current = (
        load_current
        * safety_margin
        * future_expansion_factor
    )

    for breaker in STANDARD_BREAKERS:

        if (
            breaker >= design_current
            and
            breaker <= corrected_ampacity
        ):

            device_type = determine_device_type(
                breaker
            )

            breaking_capacity = (
                determine_breaking_capacity(
                    prospective_short_circuit_ka,
                    device_type
                )
            )

            return {

                "device_type":
                    device_type,

                "rated_current_a":
                    breaker,

                "breaking_capacity_ka":
                    breaking_capacity,

                "design_current_a":
                    round(design_current, 2),

                "safety_margin":
                    safety_margin,

                "future_expansion_factor":
                    future_expansion_factor,

                "prospective_short_circuit_ka":
                    prospective_short_circuit_ka,

                "compliant":
                    True
            }

    return {

        "compliant": False,

        "message":
            "No compliant protection device found."
    }
