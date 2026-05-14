import math


STANDARD_SECTIONS_MM2 = [
    1.5, 2.5, 4, 6, 10, 16, 25, 35, 50, 70, 95, 120,
    150, 185, 240, 300, 400, 500, 630
]


BASE_AMPACITY_COPPER_XLPE = {
    1.5: 19, 2.5: 26, 4: 35, 6: 45, 10: 63, 16: 85,
    25: 112, 35: 138, 50: 168, 70: 213, 95: 258,
    120: 299, 150: 344, 185: 392, 240: 461,
    300: 530, 400: 634, 500: 729, 630: 843
}


def calculate_design_current(
    power_kw: float,
    voltage_v: float,
    power_factor: float,
    system_type: str,
    current_type: str,
    efficiency: float = 1,
    power_kva: float | None = None,
    current_a: float | None = None,
    power_input_type: str = "kw"
):

    if current_a is not None and power_input_type.lower() == "current":
        return round(current_a, 2)

    if power_input_type.lower() == "kva" and power_kva is not None:
        if current_type.upper() == "DC":
            return round((power_kva * 1000) / voltage_v, 2)

        if system_type == "three_phase":
            return round((power_kva * 1000) / (math.sqrt(3) * voltage_v), 2)

        return round((power_kva * 1000) / voltage_v, 2)

    if current_type.upper() == "DC":
        return round((power_kw * 1000) / (voltage_v * efficiency), 2)

    if system_type == "three_phase":
        current = (power_kw * 1000) / (math.sqrt(3) * voltage_v * power_factor * efficiency)
    else:
        current = (power_kw * 1000) / (voltage_v * power_factor * efficiency)

    return round(current, 2)


def material_factor(material: str):
    return 1.0 if material.lower() == "copper" else 0.78


def insulation_factor(insulation: str):
    insulation = insulation.lower()
    if insulation == "xlpe":
        return 1.0
    if insulation == "epr":
        return 0.98
    if insulation == "pvc":
        return 0.82
    return 0.9


def ambient_temperature_factor(temperature_c: float, insulation: str):

    if insulation.lower() in ["xlpe", "epr"]:
        if temperature_c <= 30:
            return 1.0
        if temperature_c <= 40:
            return 0.91
        if temperature_c <= 50:
            return 0.82
        if temperature_c <= 60:
            return 0.71
        return 0.58

    if temperature_c <= 30:
        return 1.0
    if temperature_c <= 40:
        return 0.87
    if temperature_c <= 50:
        return 0.71
    return 0.5


def grouping_factor(grouped_circuits: int):

    if grouped_circuits <= 1:
        return 1.0
    if grouped_circuits == 2:
        return 0.8
    if grouped_circuits == 3:
        return 0.7
    if grouped_circuits <= 6:
        return 0.57
    return 0.5


def installation_factor(method: str):

    method = method.lower()

    if method in ["free_air", "cable_tray", "ladder"]:
        return 1.0

    if method in ["conduit", "trunking", "duct"]:
        return 0.85

    if method in ["buried", "underground"]:
        return 0.9

    if method in ["thermal_insulation"]:
        return 0.65

    return 0.85


def harmonic_factor(thdi_percent: float):

    if thdi_percent >= 40:
        return 0.75
    if thdi_percent >= 25:
        return 0.85
    if thdi_percent >= 15:
        return 0.92
    return 1.0


def future_margin_factor(future_margin_percent: float):

    return 1 + future_margin_percent / 100


def voltage_drop_percent(
    current_a: float,
    length_m: float,
    voltage_v: float,
    section_mm2: float,
    material: str,
    power_factor: float,
    system_type: str,
    current_type: str
):

    rho = 0.0225 if material.lower() == "copper" else 0.036

    resistance = rho * length_m / section_mm2

    if current_type.upper() == "DC":
        drop_v = 2 * current_a * resistance
    elif system_type == "three_phase":
        drop_v = math.sqrt(3) * current_a * resistance * power_factor
    else:
        drop_v = 2 * current_a * resistance * power_factor

    return round((drop_v / voltage_v) * 100, 3)


def short_circuit_withstand_a(
    section_mm2: float,
    material: str,
    insulation: str,
    fault_duration_s: float
):

    material = material.lower()
    insulation = insulation.lower()

    if material == "copper" and insulation in ["xlpe", "epr"]:
        k = 143
    elif material == "copper":
        k = 115
    elif insulation in ["xlpe", "epr"]:
        k = 94
    else:
        k = 76

    return round((k * section_mm2) / math.sqrt(fault_duration_s), 2)


def neutral_recommendation(
    system_type: str,
    thdi_percent: float,
    load_type: str
):

    if system_type != "three_phase":
        return "Neutral sizing to be assessed according to circuit configuration."

    if thdi_percent >= 33 or load_type.lower() in ["ups", "data_center", "nonlinear"]:
        return "Oversized neutral conductor recommended due to nonlinear loads and triplen harmonics."

    return "Standard neutral sizing may be acceptable."


def protective_conductor_recommendation(
    section_mm2: float,
    earthing_system: str
):

    if earthing_system.upper() == "TN-C":
        return "PEN conductor requirements must be verified. Minimum PEN section rules apply."

    if section_mm2 <= 16:
        pe = section_mm2
    elif section_mm2 <= 35:
        pe = 16
    else:
        pe = section_mm2 / 2

    return f"Recommended preliminary PE section: {pe} mm². Verify with IEC rules and fault loop impedance."


def run_premium_cable_sizing(
    power_kw: float,
    voltage_v: float,
    power_factor: float,
    system_type: str,
    current_type: str,
    conductor_material: str,
    insulation_type: str,
    installation_method: str,
    ambient_temperature_c: float,
    grouped_circuits: int,
    cable_length_m: float,
    max_voltage_drop_percent: float,
    fault_current_ka: float,
    fault_duration_s: float,
    earthing_system: str,
    load_type: str,
    thdi_percent: float,
    future_margin_percent: float,
    efficiency: float = 1,
    parallel_cables: int = 1,
    power_input_type: str = "kw",
    power_kva: float | None = None,
    current_a: float | None = None
):

    design_current = calculate_design_current(
        power_kw=power_kw,
        voltage_v=voltage_v,
        power_factor=power_factor,
        system_type=system_type,
        current_type=current_type,
        efficiency=efficiency,
        power_kva=power_kva,
        current_a=current_a,
        power_input_type=power_input_type
    )

    required_current = design_current * future_margin_factor(future_margin_percent)

    correction_factor = (
        material_factor(conductor_material)
        * insulation_factor(insulation_type)
        * ambient_temperature_factor(ambient_temperature_c, insulation_type)
        * grouping_factor(grouped_circuits)
        * installation_factor(installation_method)
        * harmonic_factor(thdi_percent)
        * parallel_cables
    )

    evaluated = []
    selected = None

    for section in STANDARD_SECTIONS_MM2:

        base_ampacity = BASE_AMPACITY_COPPER_XLPE[section]

        corrected_ampacity = base_ampacity * correction_factor

        vd = voltage_drop_percent(
            current_a=design_current,
            length_m=cable_length_m,
            voltage_v=voltage_v,
            section_mm2=section,
            material=conductor_material,
            power_factor=power_factor,
            system_type=system_type,
            current_type=current_type
        )

        withstand = short_circuit_withstand_a(
            section_mm2=section,
            material=conductor_material,
            insulation=insulation_type,
            fault_duration_s=fault_duration_s
        )

        short_circuit_ok = withstand >= fault_current_ka * 1000
        ampacity_ok = corrected_ampacity >= required_current
        voltage_drop_ok = vd <= max_voltage_drop_percent

        option = {
            "section_mm2": section,
            "base_ampacity_a": base_ampacity,
            "corrected_ampacity_a": round(corrected_ampacity, 2),
            "voltage_drop_percent": vd,
            "short_circuit_withstand_a": withstand,
            "ampacity_ok": ampacity_ok,
            "voltage_drop_ok": voltage_drop_ok,
            "short_circuit_ok": short_circuit_ok,
            "compliant": ampacity_ok and voltage_drop_ok and short_circuit_ok
        }

        evaluated.append(option)

        if option["compliant"] and selected is None:
            selected = option

    recommendations = []

    if selected:
        recommendations.append("Selected cable section satisfies ampacity, voltage drop and thermal short-circuit withstand.")
    else:
        recommendations.append("No compliant standard section found. Consider parallel cables, reduced length, larger section or revised installation method.")

    if ambient_temperature_c >= 40:
        recommendations.append("High ambient temperature detected. Thermal derating applied.")

    if grouped_circuits >= 3:
        recommendations.append("Grouped circuits detected. Grouping derating applied.")

    if thdi_percent >= 15:
        recommendations.append("Harmonic distortion detected. Cable derating and neutral sizing review required.")

    if installation_method.lower() in ["buried", "underground"]:
        recommendations.append("Buried installation detected. Soil thermal resistivity and burial depth must be verified.")

    if load_type.lower() in ["motor", "vfd"]:
        recommendations.append("Motor/VFD load detected. Verify starting voltage drop, EMC, shielded cable and protection coordination.")

    recommendations.append(neutral_recommendation(system_type, thdi_percent, load_type))
    recommendations.append(protective_conductor_recommendation(selected["section_mm2"] if selected else STANDARD_SECTIONS_MM2[-1], earthing_system))
    recommendations.append("Final validation must use project standards, manufacturer data and applicable IEC installation tables.")

    return {
        "input_summary": {
            "power_kw": power_kw,
            "power_kva": power_kva,
            "current_a_input": current_a,
            "power_input_type": power_input_type,
            "voltage_v": voltage_v,
            "system_type": system_type,
            "current_type": current_type,
            "load_type": load_type,
            "earthing_system": earthing_system
        },
        "design_current_a": design_current,
        "required_current_with_margin_a": round(required_current, 2),
        "global_correction_factor": round(correction_factor, 3),
        "selected_cable": selected,
        "evaluated_options": evaluated,
        "recommendations": recommendations
    }

