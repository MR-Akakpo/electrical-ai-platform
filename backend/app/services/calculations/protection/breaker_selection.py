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
    1600
]


def select_breaker(

    load_current: float,

    corrected_ampacity: float,

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

            return {

                "breaker_rating_a":
                    breaker,

                "design_current_a":
                    round(design_current, 2),

                "safety_margin":
                    safety_margin,

                "future_expansion_factor":
                    future_expansion_factor,

                "compliant":
                    True
            }


    return {

        "compliant": False,

        "message":
            "No compliant breaker found."
    }