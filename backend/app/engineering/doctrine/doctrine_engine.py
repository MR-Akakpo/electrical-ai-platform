from typing import Dict, List


REQUIRED_STUDY_DOCUMENTS = [
    "single_line_diagram",
    "load_calculation_note",
    "voltage_drop_study",
    "short_circuit_study",
    "protection_coordination",
    "site_layout_plan",
    "equipment_datasheets",
    "grounding_study",
]


UNDERGROUND_NETWORK_RULES = {
    "minimum_depth_lv_m": 0.8,
    "minimum_depth_mv_m": 1.0,
    "warning_mesh_required": True,
    "sand_bedding_required": True,
    "cable_identification_required": True,
}


GROUNDING_RULES = {
    "max_substation_ground_resistance_ohm": 1,
    "max_industrial_ground_resistance_ohm": 5,
    "equipotential_bonding_required": True,
}


VOLTAGE_DROP_LIMITS = {
    "lighting_percent": 3,
    "power_percent": 5,
    "utility_end_percent": 10,
}


HTA_EQUIPMENT_REQUIREMENTS = {
    "surge_protection_required": True,
    "protection_relay_required": True,
    "fault_current_calculation_required": True,
    "grounding_interlock_required": True,
}


def validate_study_documents(
    provided_documents: List[str]
) -> Dict:

    missing_documents = []

    for document in REQUIRED_STUDY_DOCUMENTS:

        if document not in provided_documents:
            missing_documents.append(document)

    return {
        "required_documents": REQUIRED_STUDY_DOCUMENTS,
        "missing_documents": missing_documents,
        "compliant": len(missing_documents) == 0,
    }


def validate_voltage_drop(
    usage_type: str,
    voltage_drop_percent: float
) -> Dict:

    limit = VOLTAGE_DROP_LIMITS.get(
        usage_type,
        5
    )

    compliant = voltage_drop_percent <= limit

    return {
        "usage_type": usage_type,
        "limit_percent": limit,
        "measured_percent": voltage_drop_percent,
        "compliant": compliant,
    }


def validate_grounding_system(
    installation_type: str,
    measured_resistance_ohm: float
) -> Dict:

    if installation_type == "substation":
        limit = GROUNDING_RULES[
            "max_substation_ground_resistance_ohm"
        ]

    else:
        limit = GROUNDING_RULES[
            "max_industrial_ground_resistance_ohm"
        ]

    compliant = measured_resistance_ohm <= limit

    return {
        "installation_type": installation_type,
        "measured_resistance_ohm": measured_resistance_ohm,
        "limit_ohm": limit,
        "compliant": compliant,
    }


def validate_underground_network(
    network_type: str,
    burial_depth_m: float,
    warning_mesh: bool,
    sand_bedding: bool
) -> Dict:

    if network_type == "MV":
        minimum_depth = UNDERGROUND_NETWORK_RULES[
            "minimum_depth_mv_m"
        ]

    else:
        minimum_depth = UNDERGROUND_NETWORK_RULES[
            "minimum_depth_lv_m"
        ]

    issues = []

    if burial_depth_m < minimum_depth:
        issues.append(
            "Insufficient burial depth"
        )

    if not warning_mesh:
        issues.append(
            "Warning mesh missing"
        )

    if not sand_bedding:
        issues.append(
            "Sand bedding missing"
        )

    return {
        "network_type": network_type,
        "minimum_depth_m": minimum_depth,
        "measured_depth_m": burial_depth_m,
        "issues": issues,
        "compliant": len(issues) == 0,
    }


def validate_mv_substation(
    has_surge_protection: bool,
    has_protection_relay: bool,
    grounding_interlock: bool
) -> Dict:

    issues = []

    if not has_surge_protection:
        issues.append(
            "Surge protection missing"
        )

    if not has_protection_relay:
        issues.append(
            "Protection relay missing"
        )

    if not grounding_interlock:
        issues.append(
            "Grounding interlock missing"
        )

    return {
        "issues": issues,
        "compliant": len(issues) == 0,
    }
