import math


RESISTIVITY = {

    "copper": 0.0225,

    "aluminum": 0.036
}


REACTANCE = {

    "multicore": 0.08,

    "single_core": 0.10
}


def get_resistance(

    material: str,

    length_m: float,

    section_mm2: float
):

    resistivity = RESISTIVITY.get(
        material,
        0.0225
    )

    return (

        resistivity
        * length_m
        / section_mm2
    )


def get_reactance(

    cable_type: str,

    length_m: float
):

    reactance = REACTANCE.get(
        cable_type,
        0.08
    )

    return (
        reactance
        * length_m
        / 1000
    )


def calculate_voltage_drop(

    current: float,

    voltage: float,

    length_m: float,

    section_mm2: float,

    material: str,

    power_factor: float,

    phase: str,

    cable_type: str = "multicore"
):

    resistance = get_resistance(

        material=material,

        length_m=length_m,

        section_mm2=section_mm2
    )


    reactance = get_reactance(

        cable_type=cable_type,

        length_m=length_m
    )


    sin_phi = math.sqrt(
        1 - power_factor**2
    )


    if phase == "three":

        voltage_drop = (

            math.sqrt(3)

            * current

            * (

                resistance * power_factor
                +
                reactance * sin_phi
            )
        )

    else:

        voltage_drop = (

            2

            * current

            * (

                resistance * power_factor
                +
                reactance * sin_phi
            )
        )


    voltage_drop_percent = (

        voltage_drop
        / voltage
    ) * 100


    return {

        "resistance_ohm":
            round(resistance, 5),

        "reactance_ohm":
            round(reactance, 5),

        "voltage_drop_v":
            round(voltage_drop, 2),

        "voltage_drop_percent":
            round(voltage_drop_percent, 2)
    }