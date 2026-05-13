PROTECTION_DEVICE_TYPES = {

    "MCB": {
        "max_current_a": 125,
        "typical_breaking_capacity_ka": [6, 10, 15],
        "applications": [
            "lighting",
            "small_power",
            "residential"
        ]
    },

    "MCCB": {
        "max_current_a": 1600,
        "typical_breaking_capacity_ka": [
            25,
            36,
            50,
            70,
            100
        ],
        "applications": [
            "industrial",
            "motor",
            "distribution",
            "generator"
        ]
    },

    "ACB": {
        "max_current_a": 6300,
        "typical_breaking_capacity_ka": [
            50,
            65,
            85,
            100
        ],
        "applications": [
            "main_distribution",
            "data_center",
            "critical_power"
        ]
    },

    "FUSE": {
        "max_current_a": 1250,
        "applications": [
            "motor",
            "backup_protection"
        ]
    }
}
