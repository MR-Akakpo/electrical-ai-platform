import math

from app.engineering.cable_thermal.thermal_constants import (
    IEC_THERMAL_K_DATABASE,
    MATERIAL_ALIASES,
    INSULATION_ALIASES,
)


def normalize_material(value: str) -> str:
    return MATERIAL_ALIASES.get(
        value.lower().strip(),
        value.upper().strip(),
    )


def normalize_insulation(value: str | None) -> str | None:
    if value is None:
        return None

    return INSULATION_ALIASES.get(
        value.lower().strip(),
        value.upper().strip(),
    )


def build_lookup_key(
    material: str,
    insulation: str | None,
    arrangement: str,
) -> str:
    if arrangement == "bare_conductor_no_damage_risk":
        return material

    return f"{material}_{insulation}"


def get_verified_iec_k_factor(
    conductor_material: str,
    insulation_type: str | None,
    conductor_arrangement: str = "phase_or_pe_core_in_multicore_cable",
) -> dict:
    material = normalize_material(conductor_material)
    insulation = normalize_insulation(insulation_type)

    arrangement_data = IEC_THERMAL_K_DATABASE.get(conductor_arrangement)

    if arrangement_data is None:
        return {
            "available": False,
            "engineering_status": "UNSUPPORTED_ARRANGEMENT",
            "message": "Disposition de conducteur non disponible dans la base IEC locale verifiee.",
            "requested_arrangement": conductor_arrangement,
            "requested_material": material,
            "requested_insulation": insulation,
            "k_factor": None,
            "reference": None,
        }

    lookup_key = build_lookup_key(
        material=material,
        insulation=insulation,
        arrangement=conductor_arrangement,
    )

    values = arrangement_data["values"]

    if lookup_key not in values:
        return {
            "available": False,
            "engineering_status": "K_FACTOR_NOT_VERIFIED_LOCALLY",
            "message": (
                "Aucune valeur k IEC verifiee localement pour cette combinaison. "
                "Ne pas valider le dimensionnement final sans table normative complete "
                "ou fiche constructeur."
            ),
            "requested_key": lookup_key,
            "requested_arrangement": conductor_arrangement,
            "requested_material": material,
            "requested_insulation": insulation,
            "k_factor": None,
            "reference": arrangement_data["standard_reference"],
            "arrangement_description": arrangement_data["description"],
        }

    return {
        "available": True,
        "engineering_status": "VERIFIED_IEC_K_FACTOR",
        "requested_key": lookup_key,
        "requested_arrangement": conductor_arrangement,
        "requested_material": material,
        "requested_insulation": insulation,
        "k_factor": values[lookup_key],
        "reference": arrangement_data["standard_reference"],
        "arrangement_description": arrangement_data["description"],
    }


def calculate_required_thermal_section_mm2(
    short_circuit_current_ka: float,
    fault_duration_s: float,
    conductor_material: str,
    insulation_type: str | None,
    conductor_arrangement: str = "phase_or_pe_core_in_multicore_cable",
) -> dict:
    k_data = get_verified_iec_k_factor(
        conductor_material=conductor_material,
        insulation_type=insulation_type,
        conductor_arrangement=conductor_arrangement,
    )

    if not k_data["available"]:
        return {
            **k_data,
            "required_section_mm2": None,
            "formula": "S = I * sqrt(t) / k",
        }

    current_a = short_circuit_current_ka * 1000
    required_section = current_a * math.sqrt(fault_duration_s) / k_data["k_factor"]

    return {
        **k_data,
        "required_section_mm2": round(required_section, 2),
        "short_circuit_current_ka": short_circuit_current_ka,
        "fault_duration_s": fault_duration_s,
        "formula": "S = I * sqrt(t) / k",
    }


def calculate_permissible_short_circuit_current_ka(
    section_mm2: float,
    fault_duration_s: float,
    conductor_material: str,
    insulation_type: str | None,
    conductor_arrangement: str = "phase_or_pe_core_in_multicore_cable",
) -> dict:
    k_data = get_verified_iec_k_factor(
        conductor_material=conductor_material,
        insulation_type=insulation_type,
        conductor_arrangement=conductor_arrangement,
    )

    if not k_data["available"]:
        return {
            **k_data,
            "permissible_current_ka": None,
            "formula": "I = k * S / sqrt(t)",
        }

    current_a = k_data["k_factor"] * section_mm2 / math.sqrt(fault_duration_s)

    return {
        **k_data,
        "section_mm2": section_mm2,
        "fault_duration_s": fault_duration_s,
        "permissible_current_ka": round(current_a / 1000, 3),
        "formula": "I = k * S / sqrt(t)",
    }


def validate_thermal_withstand(
    selected_section_mm2: float,
    short_circuit_current_ka: float,
    fault_duration_s: float,
    conductor_material: str,
    insulation_type: str | None,
    conductor_arrangement: str = "phase_or_pe_core_in_multicore_cable",
) -> dict:
    required = calculate_required_thermal_section_mm2(
        short_circuit_current_ka=short_circuit_current_ka,
        fault_duration_s=fault_duration_s,
        conductor_material=conductor_material,
        insulation_type=insulation_type,
        conductor_arrangement=conductor_arrangement,
    )

    permissible = calculate_permissible_short_circuit_current_ka(
        section_mm2=selected_section_mm2,
        fault_duration_s=fault_duration_s,
        conductor_material=conductor_material,
        insulation_type=insulation_type,
        conductor_arrangement=conductor_arrangement,
    )

    if required["required_section_mm2"] is None:
        return {
            "thermal_validation": False,
            "engineering_status": "REQUIRES_STANDARD_OR_MANUFACTURER_VALIDATION",
            "selected_section_mm2": selected_section_mm2,
            "required_section_mm2": None,
            "permissible_current_ka": None,
            "details": required,
        }

    is_valid = selected_section_mm2 >= required["required_section_mm2"]

    return {
        "thermal_validation": is_valid,
        "engineering_status": (
            "THERMAL_WITHSTAND_OK"
            if is_valid
            else "THERMAL_WITHSTAND_NOT_OK"
        ),
        "selected_section_mm2": selected_section_mm2,
        "required_section_mm2": required["required_section_mm2"],
        "permissible_current_ka": permissible["permissible_current_ka"],
        "short_circuit_current_ka": short_circuit_current_ka,
        "fault_duration_s": fault_duration_s,
        "k_factor": required["k_factor"],
        "reference": required["reference"],
        "requested_key": required["requested_key"],
        "requested_arrangement": required["requested_arrangement"],
        "arrangement_description": required["arrangement_description"],
        "formula": "S = I * sqrt(t) / k",
    }
