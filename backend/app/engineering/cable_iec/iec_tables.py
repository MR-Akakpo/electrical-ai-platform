IEC_INSTALLATION_METHODS = {

    "FREE_AIR": {
        "name": "Free Air",
        "factor": 1.00,
    },

    "CABLE_TRAY": {
        "name": "Cable Tray",
        "factor": 0.95,
    },

    "LADDER": {
        "name": "Cable Ladder",
        "factor": 0.97,
    },

    "CONDUIT": {
        "name": "Conduit",
        "factor": 0.87,
    },

    "DUCT": {
        "name": "Underground Duct",
        "factor": 0.82,
    },

    "BURIED": {
        "name": "Direct Buried",
        "factor": 0.80,
    },

    "THERMAL_INSULATION": {
        "name": "Thermal Insulation",
        "factor": 0.70,
    },

    "TUNNEL": {
        "name": "Tunnel",
        "factor": 0.90,
    },
}


TEMPERATURE_FACTORS_XLPE = {

    25: 1.03,
    30: 1.00,
    35: 0.96,
    40: 0.91,
    45: 0.87,
    50: 0.82,
    55: 0.76,
}


GROUPING_FACTORS = {

    1: 1.00,
    2: 0.80,
    3: 0.70,
    4: 0.65,
    5: 0.60,
    6: 0.57,
    9: 0.52,
}


HARMONIC_FACTORS = {

    "LOW": 1.00,
    "MEDIUM": 0.90,
    "HIGH": 0.80,
    "VERY_HIGH": 0.70,
}
