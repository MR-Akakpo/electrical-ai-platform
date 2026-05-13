def analyze_trip_curve(
    breaker_curve: str,
    inrush_multiple: float
):

    breaker_curve = breaker_curve.upper()

    if breaker_curve == "B":

        threshold = 5

    elif breaker_curve == "C":

        threshold = 10

    elif breaker_curve == "D":

        threshold = 20

    else:

        threshold = 10

    if inrush_multiple <= threshold:

        return {
            "compatible": True,
            "status": "Breaker curve compatible with load inrush"
        }

    return {
        "compatible": False,
        "status": "Breaker nuisance tripping risk detected"
    }
