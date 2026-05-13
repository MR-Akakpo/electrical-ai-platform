def calculate_motor_starting_current(
    full_load_current_a: float,
    starting_method: str
):

    starting_method = starting_method.lower()

    multiplier = 6

    if starting_method == "star_delta":

        multiplier = 2

    elif starting_method == "soft_starter":

        multiplier = 3

    elif starting_method == "vfd":

        multiplier = 1.2

    starting_current = (
        full_load_current_a
        * multiplier
    )

    return {
        "starting_method": starting_method,
        "starting_current_a": round(
            starting_current,
            2
        ),
        "starting_multiplier": multiplier
    }
