IEC_GENERAL = {

    "frequency_hz": 50,

    "lv_max_voltage_v": 1000,

    "standard_voltage_levels_v": [
        230,
        400,
        415,
        690,
        11000,
        33000
    ],

    "max_voltage_drop_percent": {

        "lighting": 3,

        "power": 5,

        "critical": 2,

        "motor_starting": 10
    },

    "ambient_temperature_reference_c": {

        "pvc": 30,

        "xlpe": 30
    },

    "conductor_constants": {

        "copper": {
            "resistivity_ohm_mm2_m": 0.01724,
            "k_short_circuit": 143
        },

        "aluminum": {
            "resistivity_ohm_mm2_m": 0.0282,
            "k_short_circuit": 94
        }
    }
}
