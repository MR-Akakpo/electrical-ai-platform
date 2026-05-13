from app.engineering.short_circuit.short_circuit_engine import (
    run_short_circuit_study
)


def calculate_short_circuit_capacity(
    section_mm2: float,
    material: str,
    insulation: str,
    fault_time_s: float
):

    if material == "copper":

        k = 143

    else:

        k = 94

    short_circuit_capacity = (
        k
        * section_mm2
        / (fault_time_s ** 0.5)
    )

    engineering_fault = run_short_circuit_study(
        voltage_v=400,
        short_circuit_power_mva=500,
        transformer_power_kva=1600,
        transformer_uk_percent=6
    )

    return {

        "adiabatic_short_circuit_a":
            round(short_circuit_capacity, 2),

        "engineering_fault_study":
            engineering_fault
    }
