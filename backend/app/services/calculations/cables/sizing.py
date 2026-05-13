import math

from sqlalchemy.orm import Session

from app.engineering.cables.cable_engine import (
    run_cable_sizing_engine
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
    fault_time_s: float = 0.2,
    max_voltage_drop_percent: float = 5.0
):

    engine_result = run_cable_sizing_engine(
        db=db,
        current=current,
        voltage=voltage,
        power_factor=power_factor,
        phase=phase,
        length_m=length_m,
        temperature=temperature,
        grouping_circuits=grouping_circuits,
        installation_method=installation_method,
        material=material,
        insulation=insulation,
        cable_type=cable_type,
        fault_time_s=fault_time_s,
        max_voltage_drop_percent=max_voltage_drop_percent
    )

    if engine_result["compliant"]:

        return engine_result["selected"]

    return {
        "compliant": False,
        "message": engine_result["message"],
        "evaluated_options_count": engine_result["evaluated_options_count"]
    }
