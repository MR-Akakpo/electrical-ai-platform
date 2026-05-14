from typing import Dict, List

from app.database.engineering.equipment_database import (
    CABLE_DATABASE,
    PROTECTION_DATABASE,
)


def find_cable_by_current(
    current_a: float,
    material: str = "Copper"
):

    candidates = []

    for cable in CABLE_DATABASE:

        if (
            cable["ampacity_a"] >= current_a
            and cable["material"] == material
        ):

            candidates.append(cable)

    return candidates


def find_protection_by_current(
    current_a: float
):

    candidates = []

    for protection in PROTECTION_DATABASE:

        if protection["rating_a"] >= current_a:

            candidates.append(protection)

    return candidates


def build_engineering_recommendation(
    current_a: float,
    material: str = "Copper"
):

    cables = find_cable_by_current(
        current_a,
        material
    )

    protections = find_protection_by_current(
        current_a
    )

    return {
        "recommended_cables": cables[:3],
        "recommended_protections": protections[:3],
    }
