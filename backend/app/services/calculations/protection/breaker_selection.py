from app.engineering.protection.protection_engine import (
    select_protection_device
)


def select_breaker(
    load_current: float,
    corrected_ampacity: float,
    safety_margin: float = 1.10,
    future_expansion_factor: float = 1.20
):

    return select_protection_device(
        load_current=load_current,
        corrected_ampacity=corrected_ampacity,
        safety_margin=safety_margin,
        future_expansion_factor=future_expansion_factor
    )
