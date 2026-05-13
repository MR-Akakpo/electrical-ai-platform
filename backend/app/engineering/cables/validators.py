def validate_cable_sizing(
    current: float,
    corrected_ampacity: float,
    voltage_drop_percent: float,
    breaker_rating_a: float,
    max_voltage_drop_percent: float = 5.0
):

    ampacity_ok = corrected_ampacity >= current

    voltage_drop_ok = (
        voltage_drop_percent <= max_voltage_drop_percent
    )

    breaker_ok = (
        breaker_rating_a <= corrected_ampacity
    )

    compliant = (
        ampacity_ok
        and voltage_drop_ok
        and breaker_ok
    )

    return {
        "ampacity_ok": ampacity_ok,
        "voltage_drop_ok": voltage_drop_ok,
        "breaker_ok": breaker_ok,
        "compliant": compliant
    }
