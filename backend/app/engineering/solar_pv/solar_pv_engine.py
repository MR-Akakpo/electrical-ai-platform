def calculate_daily_energy(
    load_power_kw: float,
    operating_hours_per_day: float
):

    return round(
        load_power_kw
        * operating_hours_per_day,
        2
    )


def calculate_required_pv_power(
    daily_energy_kwh: float,
    peak_sun_hours: float,
    system_efficiency: float
):

    pv_power = (
        daily_energy_kwh
        /
        (
            peak_sun_hours
            * system_efficiency
        )
    )

    return round(pv_power, 2)


def calculate_required_battery_capacity(
    daily_energy_kwh: float,
    autonomy_days: float,
    battery_voltage_v: float,
    depth_of_discharge: float
):

    capacity_ah = (
        (
            daily_energy_kwh
            * autonomy_days
            * 1000
        )
        /
        (
            battery_voltage_v
            * depth_of_discharge
        )
    )

    return round(capacity_ah, 2)


def evaluate_inverter_sizing(
    inverter_power_kw: float,
    load_power_kw: float
):

    loading_percent = (
        load_power_kw
        / inverter_power_kw
    ) * 100

    recommendations = []

    status = "acceptable"

    if loading_percent > 100:

        status = "overloaded"

        recommendations.append(
            "Inverter overloaded."
        )

    elif loading_percent > 90:

        status = "high"

        recommendations.append(
            "Inverter heavily loaded."
        )

    else:

        recommendations.append(
            "Inverter sizing appears acceptable."
        )

    return {
        "status": status,
        "loading_percent": round(loading_percent, 2),
        "recommendations": recommendations
    }


def evaluate_hybrid_configuration(
    has_generator_backup: bool,
    has_grid_connection: bool,
    has_battery_storage: bool
):

    recommendations = []

    if has_generator_backup:

        recommendations.append(
            "Generator backup detected. Verify hybrid controller synchronization."
        )

    if has_grid_connection:

        recommendations.append(
            "Grid connection detected. Verify anti-islanding protection."
        )

    if has_battery_storage:

        recommendations.append(
            "Battery storage detected. Verify BMS and charging strategy."
        )

    return recommendations


def run_solar_pv_analysis(
    load_power_kw: float,
    operating_hours_per_day: float,
    peak_sun_hours: float,
    system_efficiency: float,
    autonomy_days: float,
    battery_voltage_v: float,
    depth_of_discharge: float,
    inverter_power_kw: float,
    has_generator_backup: bool,
    has_grid_connection: bool,
    has_battery_storage: bool
):

    daily_energy = calculate_daily_energy(
        load_power_kw=load_power_kw,
        operating_hours_per_day=operating_hours_per_day
    )

    pv_power = calculate_required_pv_power(
        daily_energy_kwh=daily_energy,
        peak_sun_hours=peak_sun_hours,
        system_efficiency=system_efficiency
    )

    battery_capacity = calculate_required_battery_capacity(
        daily_energy_kwh=daily_energy,
        autonomy_days=autonomy_days,
        battery_voltage_v=battery_voltage_v,
        depth_of_discharge=depth_of_discharge
    )

    inverter = evaluate_inverter_sizing(
        inverter_power_kw=inverter_power_kw,
        load_power_kw=load_power_kw
    )

    hybrid = evaluate_hybrid_configuration(
        has_generator_backup=has_generator_backup,
        has_grid_connection=has_grid_connection,
        has_battery_storage=has_battery_storage
    )

    recommendations = []

    recommendations.extend(
        inverter["recommendations"]
    )

    recommendations.extend(
        hybrid
    )

    recommendations.append(
        "Verify PV string voltage against inverter MPPT limits."
    )

    recommendations.append(
        "Verify DC protections, SPD and grounding."
    )

    recommendations.append(
        "Verify cable sizing and voltage drop on DC side."
    )

    return {
        "daily_energy_kwh": daily_energy,
        "required_pv_power_kwp": pv_power,
        "required_battery_capacity_ah": battery_capacity,
        "inverter_analysis": inverter,
        "recommendations": recommendations
    }
