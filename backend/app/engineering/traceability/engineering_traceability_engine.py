def build_cable_engineering_justification(
    calculation_result: dict
):

    explanations = []

    design_current =
        calculation_result.get(
            "design_current",
            0
        )

    safety_factor =
        calculation_result.get(
            "safety_factor",
            1
        )

    installation_factor =
        calculation_result.get(
            "installation_factor",
            1
        )

    temperature_factor =
        calculation_result.get(
            "temperature_factor",
            1
        )

    grouping_factor =
        calculation_result.get(
            "grouping_factor",
            1
        )

    harmonic_factor =
        calculation_result.get(
            "harmonic_factor",
            1
        )

    global_derating_factor =
        calculation_result.get(
            "global_derating_factor",
            1
        )

    selected_cable =
        calculation_result.get(
            "selected_cable",
            {}
        )

    thermal =
        calculation_result.get(
            "thermal_short_circuit_validation",
            {}
        )

    explanations.append({
        "title":
            "Base Design Current",

        "description":
            f"The electrical load current after engineering safety margin "
            f"application is {round(design_current, 2)} A.",

        "details": {
            "design_current_a":
                design_current,

            "safety_factor":
                safety_factor,
        }
    })

    explanations.append({
        "title":
            "IEC Installation Method Derating",

        "description":
            f"Installation correction factor applied: "
            f"{installation_factor}.",

        "details": {
            "installation_factor":
                installation_factor,
        }
    })

    explanations.append({
        "title":
            "Ambient Temperature Correction",

        "description":
            f"Ambient temperature derating factor: "
            f"{temperature_factor}.",

        "details": {
            "temperature_factor":
                temperature_factor,
        }
    })

    explanations.append({
        "title":
            "Grouping Correction",

        "description":
            f"Grouping correction factor applied: "
            f"{grouping_factor}.",

        "details": {
            "grouping_factor":
                grouping_factor,
        }
    })

    explanations.append({
        "title":
            "Harmonic Impact",

        "description":
            f"Harmonic derating factor applied: "
            f"{harmonic_factor}.",

        "details": {
            "harmonic_factor":
                harmonic_factor,
        }
    })

    explanations.append({
        "title":
            "Global IEC Derating",

        "description":
            f"Combined global derating factor: "
            f"{round(global_derating_factor, 3)}.",

        "details": {
            "global_derating_factor":
                global_derating_factor,
        }
    })

    if selected_cable:

        explanations.append({
            "title":
                "Selected Cable",

            "description":
                f"The selected conductor section is "
                f"{selected_cable.get('section_mm2')} mm² "
                f"with ampacity "
                f"{selected_cable.get('ampacity_a')} A.",

            "details": selected_cable
        })

    if thermal:

        explanations.append({
            "title":
                "Thermal Short-Circuit Validation",

            "description":
                (
                    "Cable thermal withstand validation PASSED."
                    if thermal.get("thermal_validation")
                    else
                    "Cable thermal withstand validation FAILED."
                ),

            "details": thermal
        })

    explanations.append({
        "title":
            "Engineering Standards",

        "description":
            "Sizing logic references IEC 60364-5-52, "
            "IEC 60364-5-54 and IEC 60949.",

        "details": {
            "references": [
                "IEC 60364-5-52",
                "IEC 60364-5-54",
                "IEC 60949",
            ]
        }
    })

    return explanations
