def calculate_total_load(
    loads: list
):

    total_kw = 0
    total_kvar = 0

    for load in loads:

        kw = load.get("power_kw", 0)
        power_factor = load.get("power_factor", 0.9)

        kva = kw / power_factor

        kvar = (
            (kva ** 2 - kw ** 2) ** 0.5
        )

        total_kw += kw
        total_kvar += kvar

    total_kva = (
        (total_kw ** 2 + total_kvar ** 2) ** 0.5
    )

    global_power_factor = (
        total_kw / total_kva
        if total_kva > 0
        else 0
    )

    return {
        "total_kw": round(total_kw, 2),
        "total_kvar": round(total_kvar, 2),
        "total_kva": round(total_kva, 2),
        "global_power_factor": round(global_power_factor, 3)
    }


def calculate_network_current(
    apparent_power_kva: float,
    voltage_v: float,
    phase: str = "three"
):

    if phase == "three":

        current = (
            apparent_power_kva * 1000
        ) / (
            1.732 * voltage_v
        )

    else:

        current = (
            apparent_power_kva * 1000
        ) / voltage_v

    return round(current, 2)


def analyze_capacity_margin(
    source_capacity_kva: float,
    total_load_kva: float
):

    loading_percent = (
        total_load_kva
        / source_capacity_kva
    ) * 100

    available_capacity_kva = (
        source_capacity_kva
        - total_load_kva
    )

    recommendations = []

    if loading_percent > 100:

        recommendations.append(
            "Source overloaded. Increase source capacity or reduce connected load."
        )

    elif loading_percent > 80:

        recommendations.append(
            "Source loading is high. Verify redundancy and future expansion margin."
        )

    elif loading_percent < 30:

        recommendations.append(
            "Source is lightly loaded. Verify economic sizing and efficiency."
        )

    else:

        recommendations.append(
            "Source loading is within a normal operating range."
        )

    return {
        "loading_percent": round(loading_percent, 2),
        "available_capacity_kva": round(available_capacity_kva, 2),
        "recommendations": recommendations
    }


def run_load_flow_analysis(
    loads: list,
    source_capacity_kva: float,
    voltage_v: float,
    phase: str = "three"
):

    load_summary = calculate_total_load(
        loads=loads
    )

    current = calculate_network_current(
        apparent_power_kva=load_summary["total_kva"],
        voltage_v=voltage_v,
        phase=phase
    )

    capacity = analyze_capacity_margin(
        source_capacity_kva=source_capacity_kva,
        total_load_kva=load_summary["total_kva"]
    )

    recommendations = []

    recommendations.extend(
        capacity["recommendations"]
    )

    if load_summary["global_power_factor"] < 0.85:

        recommendations.append(
            "Low global power factor detected. Consider reactive power compensation."
        )

    return {
        "load_summary": load_summary,
        "network_current_a": current,
        "source_capacity_kva": source_capacity_kva,
        "capacity_analysis": capacity,
        "recommendations": recommendations
    }
