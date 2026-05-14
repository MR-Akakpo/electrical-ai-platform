IEC_THERMAL_K_DATABASE = {
    "phase_or_pe_core_in_multicore_cable": {
        "description": "Conducteur incorpore dans un cable multiconducteur ou groupe avec d'autres cables/conducteurs",
        "standard_reference": "IEC 60364-5-54 Annex A, Table A.54.4 / IEC 60724",
        "values": {
            "COPPER_PVC": 115,
            "COPPER_XLPE": 143,
            "COPPER_EPR": 143,
            "ALUMINUM_PVC": 76,
            "ALUMINUM_XLPE": 94,
            "ALUMINUM_EPR": 94,
        },
    },

    "separate_insulated_conductor_or_bare_in_contact_with_sheath": {
        "description": "Conducteur isole separe ou conducteur nu en contact avec gaine de cable",
        "standard_reference": "IEC 60364-5-54 Annex A, Table A.54.4 / IEC 60724",
        "values": {
            "COPPER_PVC": 143,
            "COPPER_XLPE": 176,
            "COPPER_EPR": 176,
            "ALUMINUM_PVC": 95,
            "ALUMINUM_XLPE": 116,
            "ALUMINUM_EPR": 116,
            "STEEL_PVC": 52,
            "STEEL_XLPE": 64,
            "STEEL_EPR": 64,
        },
    },

    "metallic_layer_armour_sheath_concentric": {
        "description": "Couche metallique de cable : armure, gaine metallique, conducteur concentrique",
        "standard_reference": "IEC 60364-5-54 Annex A, Table A.54.5",
        "values": {
            "COPPER_PVC": 141,
            "COPPER_XLPE": 200,
            "COPPER_EPR": 200,
            "ALUMINUM_PVC": 93,
            "ALUMINUM_XLPE": 133,
            "ALUMINUM_EPR": 133,
            "LEAD_PVC": 26,
            "LEAD_XLPE": 31,
            "LEAD_EPR": 31,
            "STEEL_PVC": 51,
            "STEEL_XLPE": 64,
            "STEEL_EPR": 64,
        },
    },

    "bare_conductor_no_damage_risk": {
        "description": "Conducteur nu sans risque de dommage aux materiaux voisins",
        "standard_reference": "IEC 60364-5-54 Annex A, Table A.54.6",
        "values": {
            "COPPER": 159,
            "ALUMINUM": 105,
            "STEEL": 58,
        },
    },
}

MATERIAL_ALIASES = {
    "cu": "COPPER",
    "copper": "COPPER",
    "cuivre": "COPPER",
    "al": "ALUMINUM",
    "aluminum": "ALUMINUM",
    "aluminium": "ALUMINUM",
    "steel": "STEEL",
    "acier": "STEEL",
    "lead": "LEAD",
    "plomb": "LEAD",
}

INSULATION_ALIASES = {
    "pvc": "PVC",
    "xlpe": "XLPE",
    "pr": "XLPE",
    "epr": "EPR",
    "hepr": "EPR",
}
