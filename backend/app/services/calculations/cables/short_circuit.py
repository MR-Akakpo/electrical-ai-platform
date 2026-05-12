import math


K_FACTORS = {

    "copper_pvc": 115,

    "copper_xlpe": 143,

    "aluminium_pvc": 76,

    "aluminium_xlpe": 94
}


def get_k_factor(

    material: str,

    insulation: str
) -> float:

    key = f"{material}_{insulation}"

    return K_FACTORS.get(
        key,
        115
    )


def calculate_short_circuit_capacity(

    section_mm2: float,

    material: str = "copper",

    insulation: str = "xlpe",

    fault_time_s: float = 1.0
):

    """
    IEC adiabatic short-circuit withstand:

    I = k * S / sqrt(t)
    """

    k_factor = get_k_factor(
        material,
        insulation
    )


    short_circuit_current = (

        k_factor
        * section_mm2
        / math.sqrt(fault_time_s)
    )


    return {

        "k_factor":
            round(k_factor, 2),

        "fault_time_s":
            round(fault_time_s, 3),

        "short_circuit_capacity_a":
            round(short_circuit_current, 2)
    }