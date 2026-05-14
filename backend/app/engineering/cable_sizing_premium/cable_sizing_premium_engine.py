import math

from app.engineering.equipment_selection_engine import (
    build_engineering_recommendation
)

from app.engineering.cable_iec.iec_correction_engine import (
    get_installation_factor,
    get_temperature_factor,
    get_grouping_factor,
    get_harmonic_factor,
)


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
    input_mode: str,
    voltage_v: float,
    system_type: str,
    current_type: str,
    power_kw: float | None = None,
    power_kva: float | None = None,
    current_a: float | None = None,
    power_factor: float | None = None,
    efficiency: float | None = None
):

    input_mode = input_mode.lower()
    current_type = current_type.upper()
    efficiency = efficiency or 1
    power_factor = power_factor or 1

    if input_mode == "current_a":
        return round(current_a or 0, 2)

    if input_mode == "kva":
        if current_type == "DC":
            return round(((power_kva or 0) * 1000) / voltage_v, 2)

        if system_type == "three_phase":
            return round(((power_kva or 0) * 1000) / (math.sqrt(3) * voltage_v), 2)

        return round(((power_kva or 0) * 1000) / voltage_v, 2)

    if input_mode == "kw_kva":
        if power_kw and power_kva and power_kva > 0:
            inferred_pf = min(power_kw / power_kva, 1)
        else:
            inferred_pf = power_factor

        if system_type == "three_phase":
            return round(((power_kva or 0) * 1000) / (math.sqrt(3) * voltage_v), 2)

        return round(((power_kva or 0) * 1000) / voltage_v, 2)

    if current_type == "DC":
        return round(((power_kw or 0) * 1000) / (voltage_v * efficiency), 2)

    if system_type == "three_phase":
        return round(((power_kw or 0) * 1000) / (math.sqrt(3) * voltage_v * power_factor * efficiency), 2)

    return round(((power_kw or 0) * 1000) / (voltage_v * power_factor * efficiency), 2)


def material_factor(material: str):
    return 1.0 if material.lower() == "copper" else 0.78


def insulation_factor(insulation: str):
    insulation = insulation.lower()

    factors = {
        "xlpe": 1.0,
        "epr": 0.98,
        "hepr": 0.98,
        "pvc": 0.82,
        "lszh": 0.82,
        "pe": 0.9,
        "rubber": 0.88,
        "mineral": 1.05,
        "silicone": 0.95,
        "paper_oil": 0.9,
    }

    return factors.get(insulation, 0.9)


def ambient_temperature_factor(temperature_c: float, insulation: str):
    insulation = insulation.lower()

    high_temp = insulation in ["xlpe", "epr", "hepr", "silicone", "mineral"]

    if high_temp:
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

    if method in ["free_air", "perforated_tray", "ladder", "cleats"]:
        return 1.0
    if method in ["solid_tray", "conduit", "trunking", "duct", "embedded"]:
        return 0.85
    if method in ["buried", "underground", "direct_buried"]:
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


def voltage_drop_percent(current_a, length_m, voltage_v, section_mm2, material, power_factor, system_type, current_type):
    rho = 0.0225 if material.lower() == "copper" else 0.036
    resistance = rho * length_m / section_mm2
    pf = power_factor or 1

    if current_type.upper() == "DC":
        drop_v = 2 * current_a * resistance
    elif system_type == "three_phase":
        drop_v = math.sqrt(3) * current_a * resistance * pf
    else:
        drop_v = 2 * current_a * resistance * pf

    return round((drop_v / voltage_v) * 100, 3)


def short_circuit_withstand_a(section_mm2, material, insulation, fault_duration_s):
    material = material.lower()
    insulation = insulation.lower()

    if material == "copper" and insulation in ["xlpe", "epr", "hepr"]:
        k = 143
    elif material == "copper":
        k = 115
    elif insulation in ["xlpe", "epr", "hepr"]:
        k = 94
    else:
        k = 76

    return round((k * section_mm2) / math.sqrt(fault_duration_s), 2)


def load_type_recommendations(load_type: str, environment: str):
    load_type = load_type.lower()
    environment = environment.lower()
    recs = []

    if load_type in ["motor", "vfd_motor", "pump", "compressor", "fan", "conveyor"]:
        recs.append("Motor load detected. Verify starting voltage drop, overload protection and coordination.")
    if load_type in ["vfd_motor", "rectifier", "ups_input", "ev_charger", "welding", "led_lighting", "it_load"]:
        recs.append("Nonlinear load detected. Harmonic heating and neutral sizing must be reviewed.")
    if load_type in ["fire_pump", "safety_system", "emergency_lighting"]:
        recs.append("Safety-critical load detected. Fire resistance, redundancy and emergency supply rules may apply.")
    if environment in ["data_center", "hospital", "airport", "oil_gas", "mining", "marine"]:
        recs.append(f"Critical environment detected: {environment}. Apply stricter reliability, maintainability and compliance checks.")

    return recs


def run_premium_cable_sizing(
    input_mode: str = "kw",
    power_kw: float | None = None,
    power_kva: float | None = None,
    current_a: float | None = None,
    voltage_v: float = 400,
    power_factor: float | None = None,
    system_type: str = "three_phase",
    current_type: str = "AC",
    conductor_material: str = "copper",
    insulation_type: str = "xlpe",
    installation_method: str = "perforated_tray",
    ambient_temperature_c: float = 30,
    grouped_circuits: int = 1,
    cable_length_m: float = 10,
    max_voltage_drop_percent: float = 5,
    fault_current_ka: float = 10,
    fault_duration_s: float = 1,
    earthing_system: str = "TN-S",
    load_type: str = "standard",
    environment: str = "industrial",
    thdi_percent: float = 0,
    future_margin_percent: float = 20,
    efficiency: float | None = None,
    parallel_cables: int = 1
):

    design_current = calculate_design_current(
        input_mode=input_mode,
        power_kw=power_kw,
        power_kva=power_kva,
        current_a=current_a,
        voltage_v=voltage_v,
        power_factor=power_factor,
        system_type=system_type,
        current_type=current_type,
        efficiency=efficiency
    )

    required_current = design_current * (1 + future_margin_percent / 100)

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
            power_factor=power_factor or 1,
            system_type=system_type,
            current_type=current_type
        )

        withstand = short_circuit_withstand_a(
            section_mm2=section,
            material=conductor_material,
            insulation=insulation_type,
            fault_duration_s=fault_duration_s
        )

        option = {
            "section_mm2": section,
            "base_ampacity_a": base_ampacity,
            "corrected_ampacity_a": round(corrected_ampacity, 2),
            "voltage_drop_percent": vd,
            "short_circuit_withstand_a": withstand,
            "ampacity_ok": corrected_ampacity >= required_current,
            "voltage_drop_ok": vd <= max_voltage_drop_percent,
            "short_circuit_ok": withstand >= fault_current_ka * 1000,
        }

        option["compliant"] = option["ampacity_ok"] and option["voltage_drop_ok"] and option["short_circuit_ok"]
        evaluated.append(option)

        if option["compliant"] and selected is None:
            selected = option

    recommendations = []

    if selected:
        recommendations.append("Selected cable section satisfies ampacity, voltage drop and thermal short-circuit withstand.")
    else:
        recommendations.append("No compliant section found. Consider parallel cables, busbar trunking, reduced length or different installation method.")

    if input_mode == "kva":
        recommendations.append("Input based on apparent power kVA. Power factor is not required for current calculation, but remains useful for voltage drop accuracy.")
    if input_mode == "current_a":
        recommendations.append("Input based on known current. Power and power factor are not mandatory for ampacity sizing.")
    if power_factor is None:
        recommendations.append("Power factor not provided. Conservative assumptions may be used for voltage drop.")
    if efficiency is None:
        recommendations.append("Efficiency not provided. Motor/equipment efficiency should be confirmed when active power is used.")

    recommendations.extend(load_type_recommendations(load_type, environment))

    if thdi_percent >= 15:
        recommendations.append("Harmonic distortion detected. Cable derating and neutral sizing review required.")
    if earthing_system.upper() == "TN-C":
        recommendations.append("TN-C system detected. PEN conductor sizing and continuity must be verified.")
    if installation_method in ["buried", "underground", "direct_buried"]:
        recommendations.append("Buried cable detected. Soil thermal resistivity, depth and spacing must be verified.")

    recommendations.append("Final validation must use IEC installation tables, manufacturer data and local regulations.")

    equipment_selection = build_engineering_recommendation(
        current_a=design_current,
        material="Copper" if conductor_material.lower() == "copper" else "Aluminum"
    )

    engineering_justification =
        build_cable_engineering_justification({

            "design_current":
                design_current,

            "safety_factor":
                safety_factor,

            "installation_factor":
                installation_factor,

            "temperature_factor":
                temperature_factor,

            "grouping_factor":
                grouping_factor,

            "harmonic_factor":
                harmonic_factor,

            "global_derating_factor":
                global_derating_factor,

            "selected_cable":
                selected,

            "thermal_short_circuit_validation":
                thermal_validation,
        })

    return {
        "input_summary": {
            "input_mode": input_mode,
            "power_kw": power_kw,
            "power_kva": power_kva,
            "current_a": current_a,
            "voltage_v": voltage_v,
            "system_type": system_type,
            "current_type": current_type,
            "load_type": load_type,
            "environment": environment,
            "earthing_system": earthing_system
        },
        "design_current_a": design_current,
        "required_current_with_margin_a": round(required_current, 2),
        "global_correction_factor": round(correction_factor, 3),
        "selected_cable": selected,
        "recommended_equipment": equipment_selection,
        "engineering_justification":
            engineering_justification,

        "evaluated_options": evaluated,
        "recommendations": recommendations
    }



