ENGINEERING_STANDARDS = {
    "cable_sizing": [
        {
            "code": "IEC 60364-5-52",
            "title": "Selection and erection of wiring systems",
            "scope": "Cable ampacity, installation methods, voltage drop, grouping and correction factors",
            "status": "CORE_REFERENCE",
        },
        {
            "code": "IEC 60364-5-54",
            "title": "Earthing arrangements and protective conductors",
            "scope": "PE/PEN sizing, adiabatic short-circuit withstand, protective bonding",
            "status": "CORE_REFERENCE",
        },
        {
            "code": "IEC 60949",
            "title": "Calculation of thermally permissible short-circuit currents",
            "scope": "Thermal short-circuit withstand of cables",
            "status": "CORE_REFERENCE",
        },
        {
            "code": "NF C 15-100",
            "title": "Low-voltage electrical installations",
            "scope": "French LV installation rules, protection against electric shock, TT/TN/IT rules",
            "status": "LOCAL_REFERENCE",
        },
    ],

    "protection_selection": [
        {
            "code": "IEC 60947-1",
            "title": "Low-voltage switchgear and controlgear - General rules",
            "scope": "General rules for LV devices",
            "status": "CORE_REFERENCE",
        },
        {
            "code": "IEC 60947-2",
            "title": "Circuit-breakers",
            "scope": "Industrial LV circuit breakers, Icu/Ics, trip units and performance",
            "status": "CORE_REFERENCE",
        },
        {
            "code": "IEC 60947-3",
            "title": "Switches, disconnectors, switch-disconnectors and fuse-combination units",
            "scope": "Isolation and switching devices",
            "status": "CORE_REFERENCE",
        },
        {
            "code": "IEC 60947-4",
            "title": "Contactors and motor-starters",
            "scope": "Motor control and motor protection applications",
            "status": "CORE_REFERENCE",
        },
        {
            "code": "EN 60898",
            "title": "Circuit-breakers for household and similar installations",
            "scope": "Modular circuit breakers up to 125 A for non-industrial users",
            "status": "APPLICATION_REFERENCE",
        },
        {
            "code": "EN 60947-2",
            "title": "Industrial circuit-breakers",
            "scope": "Industrial circuit breaker application",
            "status": "APPLICATION_REFERENCE",
        },
    ],

    "short_circuit": [
        {
            "code": "IEC 60909",
            "title": "Short-circuit currents in three-phase AC systems",
            "scope": "Ik max/min calculation, peak current, thermal equivalent current",
            "status": "CORE_REFERENCE",
        },
        {
            "code": "IEC 60949",
            "title": "Thermally permissible short-circuit currents",
            "scope": "Cable thermal withstand verification",
            "status": "CORE_REFERENCE",
        },
    ],

    "earthing": [
        {
            "code": "IEC 60364-5-54",
            "title": "Earthing arrangements and protective conductors",
            "scope": "PE/PEN, bonding, grounding and adiabatic equation",
            "status": "CORE_REFERENCE",
        },
        {
            "code": "NF C 15-100",
            "title": "Low-voltage electrical installations",
            "scope": "TT, TN, IT protection conditions and contact protection",
            "status": "LOCAL_REFERENCE",
        },
        {
            "code": "Senelec HTA/BT Doctrine",
            "title": "Doctrine de construction des reseaux HTA et BT",
            "scope": "Network grounding, support earthing, neutral earthing, ground resistance requirements",
            "status": "UTILITY_REFERENCE",
        },
    ],

    "mv_lv_network": [
        {
            "code": "Senelec HTA/BT Doctrine",
            "title": "Doctrine de construction des reseaux HTA et BT",
            "scope": "Aerial and underground MV/LV networks, poles, grounding, surge arresters, substations",
            "status": "UTILITY_REFERENCE",
        },
        {
            "code": "IEC 60255",
            "title": "Measuring relays and protection equipment",
            "scope": "Digital protection relays for MV substations",
            "status": "CORE_REFERENCE",
        },
        {
            "code": "IEC 60051",
            "title": "Direct acting indicating analogue electrical measuring instruments",
            "scope": "Electrical measuring instruments",
            "status": "CORE_REFERENCE",
        },
    ],

    "switchboard": [
        {
            "code": "IEC 61439",
            "title": "Low-voltage switchgear and controlgear assemblies",
            "scope": "LV assemblies, TGBT, design verification, temperature rise and short-circuit withstand",
            "status": "CORE_REFERENCE",
        },
        {
            "code": "IEC 60947",
            "title": "Low-voltage switchgear and controlgear",
            "scope": "LV switching and protection devices",
            "status": "CORE_REFERENCE",
        },
    ],

    "arc_flash": [
        {
            "code": "IEEE 1584",
            "title": "Guide for Performing Arc-Flash Hazard Calculations",
            "scope": "Incident energy and arc-flash boundary calculation",
            "status": "CORE_REFERENCE",
        },
        {
            "code": "NFPA 70E",
            "title": "Electrical Safety in the Workplace",
            "scope": "Electrical safety practices and PPE categories",
            "status": "SAFETY_REFERENCE",
        },
    ],

    "solar_pv": [
        {
            "code": "IEC 62548",
            "title": "Photovoltaic arrays - Design requirements",
            "scope": "PV array design and installation",
            "status": "CORE_REFERENCE",
        },
        {
            "code": "IEC 60364-7-712",
            "title": "Requirements for special installations - Solar photovoltaic power supply systems",
            "scope": "PV electrical installation requirements",
            "status": "CORE_REFERENCE",
        },
    ],

    "audit": [
        {
            "code": "NF C 15-100",
            "title": "Low-voltage electrical installations",
            "scope": "LV installation safety and compliance audit",
            "status": "LOCAL_REFERENCE",
        },
        {
            "code": "IEC 60364",
            "title": "Low-voltage electrical installations",
            "scope": "General LV installation compliance",
            "status": "CORE_REFERENCE",
        },
        {
            "code": "Senelec HTA/BT Doctrine",
            "title": "Doctrine de construction des reseaux HTA et BT",
            "scope": "Utility network construction and acceptance criteria",
            "status": "UTILITY_REFERENCE",
        },
    ],
}


def get_standards_for_study(study_type: str):
    return {
        "study_type": study_type,
        "standards": ENGINEERING_STANDARDS.get(study_type, []),
        "status": (
            "FOUND"
            if study_type in ENGINEERING_STANDARDS
            else "NO_STANDARD_MAPPING_FOUND"
        ),
    }


def list_supported_study_types():
    return {
        "supported_study_types": sorted(ENGINEERING_STANDARDS.keys())
    }
