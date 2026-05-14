from app.engineering.cable_iec.iec_tables import (
    IEC_INSTALLATION_METHODS,
    TEMPERATURE_FACTORS_XLPE,
    GROUPING_FACTORS,
    HARMONIC_FACTORS,
)


def get_installation_factor(
    method: str
):

    return IEC_INSTALLATION_METHODS.get(
        method,
        {"factor": 1.0}
    )["factor"]


def get_temperature_factor(
    ambient_temp: float
):

    closest = min(
        TEMPERATURE_FACTORS_XLPE.keys(),
        key=lambda x: abs(x - ambient_temp)
    )

    return TEMPERATURE_FACTORS_XLPE[closest]


def get_grouping_factor(
    circuits: int
):

    available = sorted(
        GROUPING_FACTORS.keys()
    )

    selected = available[-1]

    for value in available:

        if circuits <= value:

            selected = value
            break

    return GROUPING_FACTORS[selected]


def get_harmonic_factor(
    level: str
):

    return HARMONIC_FACTORS.get(
        level,
        1.0
    )
