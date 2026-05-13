from sqlalchemy.orm import Session

from app.repositories.cable_repository import (
    get_cables
)

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

from app.services.calculations.protection.breaker_selection import (
    select_breaker
)

from app.engineering.cables.validators import (
    validate_cable_sizing
)

from app.engineering.cables.recommendations import (
    generate_cable_recommendations
)

from app.standards.iec.iec_general import (
    IEC_GENERAL
)
    generate_cable_recommendations
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


def run_cable_sizing_engine(
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

    cables = get_cables(
        db=db,
        material=material,
        installation_method=installation_method
    )

    installation_factor = installation_method_factor(
        installation_method
    )

    evaluated_options = []

    for cable in cables:

        base_ampacity = get_ampacity(
            db=db,
            section_mm2=cable.section_mm2,
            material=material,
            insulation=insulation,
            installation_method=installation_method
        )

        if base_ampacity <= 0:
            continue

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

        voltage_drop = calculate_voltage_drop(
            current=current,
            voltage=voltage,
            length_m=length_m,
            section_mm2=cable.section_mm2,
            material=material,
            power_factor=power_factor,
            phase=phase,
            cable_type=cable_type
        )

        short_circuit = calculate_short_circuit_capacity(
            section_mm2=cable.section_mm2,
            material=material,
            insulation=insulation,
            fault_time_s=fault_time_s
        )

        validation = validate_cable_sizing(
            current=current,
            corrected_ampacity=corrected_ampacity,
            voltage_drop_percent=voltage_drop["voltage_drop_percent"],
            breaker_rating_a=breaker_data["breaker_rating_a"],
            max_voltage_drop_percent=max_voltage_drop_percent
        )

        recommendations = generate_cable_recommendations(
            voltage_drop_percent=voltage_drop["voltage_drop_percent"],
            corrected_ampacity=corrected_ampacity,
            current=current,
            breaker_rating_a=breaker_data["breaker_rating_a"],
            material=material,
            max_voltage_drop_percent=max_voltage_drop_percent
        )

        option = {
            "section_mm2": cable.section_mm2,
            "ampacity": base_ampacity,
            "corrected_ampacity": round(corrected_ampacity, 2),
            "recommended_breaker_a": breaker_data["breaker_rating_a"],
            "breaker": breaker_data,
            "short_circuit": short_circuit,
            "material": material,
            "insulation": insulation,
            "cable_type": cable_type,
            "installation_method": installation_method,
            "voltage_drop": voltage_drop,
            "validation": validation,
            "recommendations": recommendations
        }

        evaluated_options.append(option)

        if validation["compliant"]:
            return {
                "selected": option,
                "evaluated_options_count": len(evaluated_options),
                "compliant": True
            }

    return {
        "selected": None,
        "evaluated_options_count": len(evaluated_options),
        "compliant": False,
        "message": "No compliant cable found for the provided engineering assumptions."
    }
