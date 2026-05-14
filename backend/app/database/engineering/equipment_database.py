CABLE_DATABASE = [

    {
        "material": "Copper",
        "insulation": "XLPE",
        "section_mm2": 1.5,
        "ampacity_a": 19,
        "resistance_ohm_km": 12.1,
        "reactance_ohm_km": 0.08,
        "voltage_class": "LV",
    },

    {
        "material": "Copper",
        "insulation": "XLPE",
        "section_mm2": 2.5,
        "ampacity_a": 26,
        "resistance_ohm_km": 7.41,
        "reactance_ohm_km": 0.08,
        "voltage_class": "LV",
    },

    {
        "material": "Copper",
        "insulation": "XLPE",
        "section_mm2": 4,
        "ampacity_a": 35,
        "resistance_ohm_km": 4.61,
        "reactance_ohm_km": 0.08,
        "voltage_class": "LV",
    },

    {
        "material": "Copper",
        "insulation": "XLPE",
        "section_mm2": 6,
        "ampacity_a": 44,
        "resistance_ohm_km": 3.08,
        "reactance_ohm_km": 0.08,
        "voltage_class": "LV",
    },

    {
        "material": "Copper",
        "insulation": "XLPE",
        "section_mm2": 10,
        "ampacity_a": 61,
        "resistance_ohm_km": 1.83,
        "reactance_ohm_km": 0.08,
        "voltage_class": "LV",
    },

    {
        "material": "Copper",
        "insulation": "XLPE",
        "section_mm2": 16,
        "ampacity_a": 82,
        "resistance_ohm_km": 1.15,
        "reactance_ohm_km": 0.08,
        "voltage_class": "LV",
    },

    {
        "material": "Copper",
        "insulation": "XLPE",
        "section_mm2": 25,
        "ampacity_a": 109,
        "resistance_ohm_km": 0.727,
        "reactance_ohm_km": 0.08,
        "voltage_class": "LV",
    },

    {
        "material": "Copper",
        "insulation": "XLPE",
        "section_mm2": 35,
        "ampacity_a": 135,
        "resistance_ohm_km": 0.524,
        "reactance_ohm_km": 0.08,
        "voltage_class": "LV",
    },

    {
        "material": "Copper",
        "insulation": "XLPE",
        "section_mm2": 50,
        "ampacity_a": 167,
        "resistance_ohm_km": 0.387,
        "reactance_ohm_km": 0.08,
        "voltage_class": "LV",
    },

    {
        "material": "Aluminum",
        "insulation": "XLPE",
        "section_mm2": 50,
        "ampacity_a": 129,
        "resistance_ohm_km": 0.641,
        "reactance_ohm_km": 0.08,
        "voltage_class": "LV",
    },
]


PROTECTION_DATABASE = [

    {
        "device_type": "MCB",
        "curve": "B",
        "rating_a": 6,
        "breaking_capacity_ka": 6,
        "application": "Lighting",
    },

    {
        "device_type": "MCB",
        "curve": "C",
        "rating_a": 16,
        "breaking_capacity_ka": 6,
        "application": "General Power",
    },

    {
        "device_type": "MCB",
        "curve": "D",
        "rating_a": 32,
        "breaking_capacity_ka": 10,
        "application": "Motor Loads",
    },

    {
        "device_type": "MCCB",
        "curve": "Thermal Magnetic",
        "rating_a": 100,
        "breaking_capacity_ka": 25,
        "application": "Industrial Distribution",
    },

    {
        "device_type": "ACB",
        "curve": "LSIG",
        "rating_a": 1600,
        "breaking_capacity_ka": 65,
        "application": "Main LV Switchboard",
    },

    {
        "device_type": "Fuse",
        "curve": "gG",
        "rating_a": 125,
        "breaking_capacity_ka": 80,
        "application": "Cable Protection",
    },

    {
        "device_type": "MV Relay",
        "curve": "IEC Standard Inverse",
        "rating_a": 630,
        "breaking_capacity_ka": 25,
        "application": "MV Protection",
    },
]
