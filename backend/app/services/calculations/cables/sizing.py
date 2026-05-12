import math

from sqlalchemy.orm import Session

from app.repositories.cable_repository import (
    get_cables
)

from app.services.calculations.cables.ampacity import (
    get_ampacity
)

from app.services.calculations.cables.voltage_drop import (
    calculate_voltage_drop
)

from app.services.calculations.cables.short_circuit import (
    calculate_short_circuit_capacity
)

from app.services.calculations.cables.correction_factors import (
    apply_correction_factors
)

from app.services.calculations.protection.breaker_selection import (
    select_breaker
)


def calculate_current(

    power_kw: float,

    voltage: float,

    power_factor: float,

    phase: str
):

    if phase == "three":

        current = (

            power_kw * 1000
        ) / (

            math.sqrt(3)
            * voltage
            * power_factor
        )

    else:

        current = (

            power_kw * 1000
        ) / (

            voltage
            * power_factor
        )

    return round(current, 2)


def calculate_apparent_power(

    power_kw: float,

    power_factor: float
):

    apparent_power = (
        power_kw / power_factor
    )

    return round(
        apparent_power,
        2
    )


def installation_method_factor(

    method: str
):

    factors = {

        "A": 0.89,

        "B": 0.94,

        "C": 1.0,

        "D": 1.12
    }

    return factors.get(
        method,
        1.0
    )


def generate_recommendations(

    voltage_drop_percent: float,

    corrected_ampacity: float,

    current: float,

    breaker: float,

    material: str
):

    recommendations = []

    if voltage_drop_percent > 3:

        recommendations.append(
            "Voltage drop is relatively high. Consider increasing cable section."
        )

    if material == "aluminum":

        recommendations.append(
            "Aluminum cable selected. Verify terminal compatibility and mechanical constraints."
        )

    ampacity_margin = (
        corrected_ampacity - current
    )

    if ampacity_margin < 10:

        recommendations.append(
            "Low ampacity margin detected. Consider higher cable section for future expansion."
        )

    if breaker > corrected_ampacity:

        recommendations.append(
            "Breaker rating exceeds corrected cable ampacity."
        )

    if not recommendations:

        recommendations.append(
            "Cable sizing appears optimized and compliant."
        )

    return recommendations


def validate_cable(

    current: float,

    corrected_ampacity: float,

    voltage_drop_percent: float,

    breaker: float
):

    ampacity_ok = (
        corrected_ampacity >= current
    )

    voltage_drop_ok = (
        voltage_drop_percent <= 5
    )

    breaker_ok = (
        breaker <= corrected_ampacity
    )

    return {

        "ampacity_ok": ampacity_ok,

        "voltage_drop_ok": voltage_drop_ok,

        "breaker_ok": breaker_ok,

        "compliant": (

            ampacity_ok
            and
            voltage_drop_ok
            and
            breaker_ok
        )
    }


def optimize_cable_section(

    db: Session,

    current: float,

    voltage: float,

    power_factor: float,

    phase: str,

    length_m: float,

    temperature: int,

    grouping_circuits: int,

    installation_method: str,

    material: str,

    insulation: str = "xlpe",

    cable_type: str = "multicore",

    fault_time_s: float = 0.2
):

    cables = get_cables(

        db=db,

        material=material,

        installation_method=installation_method
    )

    installation_factor = (
        installation_method_factor(
            installation_method
        )
    )

    for cable in cables:

        base_ampacity = (

            get_ampacity(

                db=db,

                section_mm2=cable.section_mm2,

                material=material,

                insulation=insulation,

                installation_method=installation_method
            )
        )


        corrected_ampacity = (

            apply_correction_factors(

                db=db,

                ampacity=base_ampacity,

                temperature=temperature,

                circuits=grouping_circuits
            )

            * installation_factor
        )


        breaker_data = select_breaker(

            load_current=current,

            corrected_ampacity=corrected_ampacity
        )


        if not breaker_data["compliant"]:

            continue


        voltage_drop = (
            calculate_voltage_drop(

                current=current,

                voltage=voltage,

                length_m=length_m,

                section_mm2=cable.section_mm2,

                material=material,

                power_factor=power_factor,

                phase=phase,

                cable_type=cable_type
            )
        )


        short_circuit = (
            calculate_short_circuit_capacity(

                section_mm2=cable.section_mm2,

                material=material,

                insulation=insulation,

                fault_time_s=fault_time_s
            )
        )


        validation = validate_cable(

            current=current,

            corrected_ampacity=corrected_ampacity,

            voltage_drop_percent=voltage_drop[
                "voltage_drop_percent"
            ],

            breaker=breaker_data[
                "breaker_rating_a"
            ]
        )


        recommendations = (

            generate_recommendations(

                voltage_drop_percent=voltage_drop[
                    "voltage_drop_percent"
                ],

                corrected_ampacity=corrected_ampacity,

                current=current,

                breaker=breaker_data[
                    "breaker_rating_a"
                ],

                material=material
            )
        )


        if validation["compliant"]:

            return {

                "section_mm2":
                    cable.section_mm2,

                "ampacity":
                    base_ampacity,

                "corrected_ampacity":
                    round(corrected_ampacity, 2),

                "recommended_breaker_a":

                    breaker_data[
                        "breaker_rating_a"
                    ],

                "short_circuit":
                    short_circuit,

                "material":
                    material,

                "voltage_drop":
                    voltage_drop,

                "validation":
                    validation,

                "recommendations":
                    recommendations
            }

    return {

        "compliant": False,

        "message":
            "No compliant cable found."
    }