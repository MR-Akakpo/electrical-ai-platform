from app.services.calculations.cables.ampacity import (
    get_ampacity
)

from app.services.calculations.cables.correction_factors import (
    apply_correction_factors
)

from app.services.calculations.cables.voltage_drop import (
    calculate_voltage_drop
)

from app.services.calculations.cables.short_circuit import (
    calculate_short_circuit_capacity
)


AVAILABLE_SECTIONS = [

    1.5,
    2.5,
    4,
    6,
    10,
    16,
    25,
    35,
    50,
    70,
    95,
    120,
    150,
    185,
    240
]


def select_cable(

    current: float,

    voltage: float,

    phase: str,

    length_m: float,

    material: str,

    installation_method: str,

    temperature: int,

    grouping_circuits: int,

    max_voltage_drop_percent: float = 5.0,

    fault_time_s: float = 1.0,

    insulation: str = "xlpe"
):

    for section in AVAILABLE_SECTIONS:

        base_ampacity = get_ampacity(

            section_mm2=section,

            material=material,

            installation_method=installation_method
        )


        corrected_ampacity = (
            apply_correction_factors(

                ampacity=base_ampacity,

                temperature=temperature,

                circuits=grouping_circuits
            )
        )


        voltage_drop = (
            calculate_voltage_drop(

                current=current,

                length_m=length_m,

                section_mm2=section,

                voltage=voltage,

                phase=phase
            )
        )


        short_circuit = (
            calculate_short_circuit_capacity(

                section_mm2=section,

                material=material,

                insulation=insulation,

                fault_time_s=fault_time_s
            )
        )


        ampacity_ok = (
            corrected_ampacity >= current
        )

        voltage_drop_ok = (

            voltage_drop["voltage_drop_percent"]
            <= max_voltage_drop_percent
        )


        short_circuit_ok = (

            short_circuit[
                "short_circuit_capacity_a"
            ] > current * 10
        )


        if (

            ampacity_ok
            and voltage_drop_ok
            and short_circuit_ok
        ):

            return {

                "section_mm2":
                    section,

                "base_ampacity":
                    base_ampacity,

                "corrected_ampacity":
                    corrected_ampacity,

                "voltage_drop":
                    voltage_drop,

                "short_circuit":
                    short_circuit,

                "validation": {

                    "ampacity_ok":
                        ampacity_ok,

                    "voltage_drop_ok":
                        voltage_drop_ok,

                    "short_circuit_ok":
                        short_circuit_ok,

                    "compliant": True
                }
            }


    return {

        "compliant": False,

        "message":
            "No compliant cable found."
    }