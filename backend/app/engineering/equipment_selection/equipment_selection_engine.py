from app.engineering.equipment_selection.equipment_catalog import (
    EQUIPMENT_TYPES
)

from app.engineering.equipment_selection.equipment_rules import (
    select_equipment_family,
    determine_protection_device_type,
    determine_switchgear_type,
    generate_equipment_recommendations
)


def run_equipment_selection(
    application: str,
    load_type: str,
    load_current_a: float,
    voltage_level: str,
    current_type: str,
    short_circuit_level_ka: float,
    criticality: str = "standard"
):

    families = select_equipment_family(
        application=application,
        load_type=load_type,
        voltage_level=voltage_level,
        current_type=current_type
    )

    equipment_candidates = {}

    for family in families:

        equipment_candidates[family] = EQUIPMENT_TYPES.get(
            family,
            []
        )

    protection_type = determine_protection_device_type(
        load_current_a=load_current_a,
        voltage_level=voltage_level
    )

    switchgear_type = determine_switchgear_type(
        voltage_level=voltage_level,
        criticality=criticality
    )

    recommendations = generate_equipment_recommendations(
        application=application,
        load_type=load_type,
        load_current_a=load_current_a,
        voltage_level=voltage_level,
        current_type=current_type,
        short_circuit_level_ka=short_circuit_level_ka,
        criticality=criticality
    )

    return {
        "application": application,
        "load_type": load_type,
        "voltage_level": voltage_level,
        "current_type": current_type,
        "load_current_a": load_current_a,
        "short_circuit_level_ka": short_circuit_level_ka,
        "criticality": criticality,
        "selected_families": families,
        "equipment_candidates": equipment_candidates,
        "recommended_protection_type": protection_type,
        "recommended_switchgear_type": switchgear_type,
        "recommendations": recommendations
    }
