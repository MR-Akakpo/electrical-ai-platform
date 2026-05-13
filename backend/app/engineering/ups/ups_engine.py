def calculate_ups_required_capacity(
    critical_load_kw: float,
    power_factor: float,
    redundancy_factor: float = 1.2
):

    apparent_power_kva = (
        critical_load_kw
        / power_factor
    )

    required_capacity = (
        apparent_power_kva
        * redundancy_factor
    )

    return round(
        required_capacity,
        2
    )


def calculate_battery_autonomy_minutes(
    battery_energy_kwh: float,
    critical_load_kw: float
):

    if critical_load_kw <= 0:

        return 0

    autonomy_hours = (
        battery_energy_kwh
        / critical_load_kw
    )

    autonomy_minutes = (
        autonomy_hours
        * 60
    )

    return round(
        autonomy_minutes,
        2
    )


def analyze_ups_redundancy(
    redundancy_topology: str
):

    recommendations = []

    if redundancy_topology == "N":

        recommendations.append(
            "N topology has no redundancy. Consider N+1 or 2N for critical data center applications."
        )

    elif redundancy_topology == "N+1":

        recommendations.append(
            "N+1 redundancy provides improved availability for critical loads."
        )

    elif redundancy_topology == "2N":

        recommendations.append(
            "2N redundancy provides high resilience with independent power paths."
        )

    else:

        recommendations.append(
            "Unknown redundancy topology. Verify system architecture."
        )

    return recommendations


def run_ups_analysis(
    critical_load_kw: float,
    power_factor: float,
    battery_energy_kwh: float,
    redundancy_topology: str = "N+1",
    redundancy_factor: float = 1.2
):

    required_capacity_kva = calculate_ups_required_capacity(
        critical_load_kw=critical_load_kw,
        power_factor=power_factor,
        redundancy_factor=redundancy_factor
    )

    autonomy_minutes = calculate_battery_autonomy_minutes(
        battery_energy_kwh=battery_energy_kwh,
        critical_load_kw=critical_load_kw
    )

    recommendations = analyze_ups_redundancy(
        redundancy_topology=redundancy_topology
    )

    if autonomy_minutes < 10:

        recommendations.append(
            "Battery autonomy is low for critical infrastructure. Verify site requirements."
        )

    if power_factor < 0.9:

        recommendations.append(
            "Low power factor detected. Verify UPS output capacity and load characteristics."
        )

    return {
        "critical_load_kw": critical_load_kw,
        "required_ups_capacity_kva": required_capacity_kva,
        "battery_autonomy_minutes": autonomy_minutes,
        "redundancy_topology": redundancy_topology,
        "recommendations": recommendations
    }
