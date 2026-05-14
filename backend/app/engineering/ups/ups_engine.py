def calculate_ups_load_percent(
    ups_power_kva: float,
    connected_load_kva: float
):

    load_percent = (
        connected_load_kva
        / ups_power_kva
    ) * 100

    return round(load_percent, 2)


def evaluate_ups_loading(
    load_percent: float
):

    status = "acceptable"

    recommendations = []

    if load_percent > 100:

        status = "overloaded"

        recommendations.append(
            "UPS overloaded. Increase UPS capacity or reduce connected load."
        )

    elif load_percent > 80:

        status = "high"

        recommendations.append(
            "UPS heavily loaded. Verify future expansion and redundancy."
        )

    elif load_percent < 20:

        status = "low"

        recommendations.append(
            "UPS lightly loaded. Verify efficiency and modular optimization."
        )

    else:

        recommendations.append(
            "UPS loading appears acceptable."
        )

    return {
        "status": status,
        "load_percent": load_percent,
        "recommendations": recommendations
    }


def calculate_battery_autonomy(
    battery_voltage_v: float,
    battery_capacity_ah: float,
    dc_bus_efficiency: float,
    connected_load_kw: float
):

    energy_kwh = (
        battery_voltage_v
        * battery_capacity_ah
    ) / 1000

    usable_energy = (
        energy_kwh
        * dc_bus_efficiency
    )

    autonomy_hours = (
        usable_energy
        / connected_load_kw
    )

    return round(autonomy_hours, 2)


def evaluate_redundancy(
    redundancy_type: str
):

    recommendations = []

    redundancy_type = redundancy_type.upper()

    if redundancy_type == "N+1":

        recommendations.append(
            "UPS N+1 redundancy detected."
        )

    elif redundancy_type == "2N":

        recommendations.append(
            "UPS 2N architecture detected. High resilience configuration."
        )

    elif redundancy_type == "N":

        recommendations.append(
            "No UPS redundancy detected."
        )

    else:

        recommendations.append(
            "Custom UPS redundancy configuration detected."
        )

    return recommendations


def evaluate_bypass_configuration(
    has_static_bypass: bool,
    has_maintenance_bypass: bool
):

    recommendations = []

    if has_static_bypass:

        recommendations.append(
            "Static bypass available."
        )

    else:

        recommendations.append(
            "No static bypass detected."
        )

    if has_maintenance_bypass:

        recommendations.append(
            "Maintenance bypass available."
        )

    else:

        recommendations.append(
            "Maintenance bypass recommended for maintainability."
        )

    return recommendations


def run_ups_analysis(
    ups_power_kva: float,
    connected_load_kva: float,
    connected_load_kw: float,
    battery_voltage_v: float,
    battery_capacity_ah: float,
    dc_bus_efficiency: float,
    redundancy_type: str,
    has_static_bypass: bool,
    has_maintenance_bypass: bool,
    application: str,
    battery_type: str
):

    load_percent = calculate_ups_load_percent(
        ups_power_kva=ups_power_kva,
        connected_load_kva=connected_load_kva
    )

    loading = evaluate_ups_loading(
        load_percent=load_percent
    )

    autonomy = calculate_battery_autonomy(
        battery_voltage_v=battery_voltage_v,
        battery_capacity_ah=battery_capacity_ah,
        dc_bus_efficiency=dc_bus_efficiency,
        connected_load_kw=connected_load_kw
    )

    redundancy = evaluate_redundancy(
        redundancy_type=redundancy_type
    )

    bypass = evaluate_bypass_configuration(
        has_static_bypass=has_static_bypass,
        has_maintenance_bypass=has_maintenance_bypass
    )

    recommendations = []

    recommendations.extend(
        loading["recommendations"]
    )

    recommendations.extend(
        redundancy
    )

    recommendations.extend(
        bypass
    )

    if battery_type.lower() == "lithium":

        recommendations.append(
            "Lithium battery technology detected. Verify BMS integration and thermal management."
        )

    if battery_type.lower() == "vrla":

        recommendations.append(
            "VRLA batteries detected. Verify room ventilation and temperature control."
        )

    if application.lower() == "data_center":

        recommendations.append(
            "Data center application detected. Verify STS coordination and dual-cord architecture."
        )

    recommendations.append(
        "Verify harmonics, selectivity, grounding and downstream coordination."
    )

    return {
        "ups_power_kva": ups_power_kva,
        "load_analysis": loading,
        "battery_autonomy_hours": autonomy,
        "recommendations": recommendations
    }
