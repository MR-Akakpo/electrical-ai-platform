def calculate_daily_energy_need(
    daily_consumption_kwh: float,
    system_losses_percent: float
):

    corrected_energy = (
        daily_consumption_kwh
        / (1 - system_losses_percent / 100)
    )

    return round(corrected_energy, 2)


def calculate_required_pv_power_kwp(
    corrected_daily_energy_kwh: float,
    peak_sun_hours: float,
    performance_ratio: float
):

    pv_power_kwp = (
        corrected_daily_energy_kwh
        /
        (
            peak_sun_hours
            * performance_ratio
        )
    )

    return round(pv_power_kwp, 2)


def calculate_number_of_modules(
    required_pv_kwp: float,
    module_power_wp: float
):

    modules = (
        required_pv_kwp
        * 1000
    ) / module_power_wp

    return int(modules) + 1


def analyze_string_configuration(
    modules_count: int,
    module_voc_v: float,
    module_vmp_v: float,
    inverter_max_dc_voltage_v: float,
    inverter_mppt_min_v: float,
    inverter_mppt_max_v: float,
    temperature_correction_factor: float = 1.15
):

    max_modules_series_by_voc = int(
        inverter_max_dc_voltage_v
        /
        (
            module_voc_v
            * temperature_correction_factor
        )
    )

    max_modules_series_by_mppt = int(
        inverter_mppt_max_v
        /
        module_vmp_v
    )

    min_modules_series_by_mppt = int(
        inverter_mppt_min_v
        /
        module_vmp_v
    ) + 1

    recommended_modules_series = min(
        max_modules_series_by_voc,
        max_modules_series_by_mppt
    )

    if recommended_modules_series <= 0:

        recommended_modules_series = 1

    parallel_strings = int(
        modules_count
        / recommended_modules_series
    )

    if modules_count % recommended_modules_series != 0:

        parallel_strings += 1

    return {
        "modules_count": modules_count,
        "recommended_modules_in_series": recommended_modules_series,
        "recommended_parallel_strings": parallel_strings,
        "min_modules_series_mppt": min_modules_series_by_mppt,
        "max_modules_series_voc": max_modules_series_by_voc,
        "max_modules_series_mppt": max_modules_series_by_mppt
    }


def analyze_inverter_sizing(
    pv_power_kwp: float,
    inverter_ac_power_kw: float
):

    dc_ac_ratio = (
        pv_power_kwp
        / inverter_ac_power_kw
    )

    recommendations = []

    if dc_ac_ratio > 1.35:

        recommendations.append(
            "High DC/AC ratio detected. Verify clipping losses and inverter overload capability."
        )

    elif dc_ac_ratio < 0.9:

        recommendations.append(
            "Inverter may be oversized compared to PV array."
        )

    else:

        recommendations.append(
            "PV DC/AC ratio is within a typical engineering range."
        )

    return {
        "dc_ac_ratio": round(dc_ac_ratio, 2),
        "recommendations": recommendations
    }


def calculate_battery_capacity_required(
    daily_consumption_kwh: float,
    autonomy_days: float,
    depth_of_discharge: float,
    battery_efficiency: float
):

    capacity = (
        daily_consumption_kwh
        * autonomy_days
    ) / (
        depth_of_discharge
        * battery_efficiency
    )

    return round(capacity, 2)


def analyze_bess_autonomy(
    battery_capacity_kwh: float,
    critical_load_kw: float,
    depth_of_discharge: float,
    battery_efficiency: float
):

    usable_energy = (
        battery_capacity_kwh
        * depth_of_discharge
        * battery_efficiency
    )

    autonomy_hours = (
        usable_energy
        / critical_load_kw
    )

    return round(autonomy_hours, 2)


def generate_pv_bess_recommendations(
    dc_ac_ratio: float,
    battery_autonomy_hours: float,
    system_type: str,
    has_generator_backup: bool,
    parallel_strings: int
):

    recommendations = []

    recommendations.append(
        "Verify DC string protection, DC isolators, SPD Type 2 DC and AC surge protection."
    )

    recommendations.append(
        "Verify earthing, equipotential bonding, inverter anti-islanding and grid code requirements."
    )

    if parallel_strings >= 3:

        recommendations.append(
            "Multiple parallel strings detected. String fusing or combiner protection may be required."
        )

    if battery_autonomy_hours < 2:

        recommendations.append(
            "Battery autonomy is low for critical applications. Verify project autonomy target."
        )

    if system_type == "hybrid":

        recommendations.append(
            "Hybrid PV/BESS system detected. Verify generator, inverter and battery control coordination."
        )

    if has_generator_backup:

        recommendations.append(
            "Generator backup detected. Verify reverse power, load sharing and PV curtailment strategy."
        )

    if dc_ac_ratio > 1.35:

        recommendations.append(
            "Consider reducing PV oversizing or selecting larger inverter capacity."
        )

    return recommendations


def run_solar_bess_analysis(
    daily_consumption_kwh: float,
    peak_sun_hours: float,
    module_power_wp: float,
    module_voc_v: float,
    module_vmp_v: float,
    inverter_ac_power_kw: float,
    inverter_max_dc_voltage_v: float,
    inverter_mppt_min_v: float,
    inverter_mppt_max_v: float,
    battery_capacity_kwh: float,
    critical_load_kw: float,
    autonomy_days: float = 1,
    performance_ratio: float = 0.8,
    system_losses_percent: float = 14,
    depth_of_discharge: float = 0.8,
    battery_efficiency: float = 0.9,
    temperature_correction_factor: float = 1.15,
    system_type: str = "hybrid",
    has_generator_backup: bool = False
):

    corrected_energy = calculate_daily_energy_need(
        daily_consumption_kwh=daily_consumption_kwh,
        system_losses_percent=system_losses_percent
    )

    required_pv_kwp = calculate_required_pv_power_kwp(
        corrected_daily_energy_kwh=corrected_energy,
        peak_sun_hours=peak_sun_hours,
        performance_ratio=performance_ratio
    )

    modules_count = calculate_number_of_modules(
        required_pv_kwp=required_pv_kwp,
        module_power_wp=module_power_wp
    )

    string_config = analyze_string_configuration(
        modules_count=modules_count,
        module_voc_v=module_voc_v,
        module_vmp_v=module_vmp_v,
        inverter_max_dc_voltage_v=inverter_max_dc_voltage_v,
        inverter_mppt_min_v=inverter_mppt_min_v,
        inverter_mppt_max_v=inverter_mppt_max_v,
        temperature_correction_factor=temperature_correction_factor
    )

    inverter_analysis = analyze_inverter_sizing(
        pv_power_kwp=required_pv_kwp,
        inverter_ac_power_kw=inverter_ac_power_kw
    )

    required_battery_capacity = calculate_battery_capacity_required(
        daily_consumption_kwh=daily_consumption_kwh,
        autonomy_days=autonomy_days,
        depth_of_discharge=depth_of_discharge,
        battery_efficiency=battery_efficiency
    )

    actual_battery_autonomy = analyze_bess_autonomy(
        battery_capacity_kwh=battery_capacity_kwh,
        critical_load_kw=critical_load_kw,
        depth_of_discharge=depth_of_discharge,
        battery_efficiency=battery_efficiency
    )

    recommendations = generate_pv_bess_recommendations(
        dc_ac_ratio=inverter_analysis["dc_ac_ratio"],
        battery_autonomy_hours=actual_battery_autonomy,
        system_type=system_type,
        has_generator_backup=has_generator_backup,
        parallel_strings=string_config["recommended_parallel_strings"]
    )

    recommendations.extend(
        inverter_analysis["recommendations"]
    )

    return {
        "energy_analysis": {
            "daily_consumption_kwh": daily_consumption_kwh,
            "corrected_daily_energy_kwh": corrected_energy,
            "peak_sun_hours": peak_sun_hours,
            "performance_ratio": performance_ratio,
            "system_losses_percent": system_losses_percent
        },
        "pv_array_sizing": {
            "required_pv_power_kwp": required_pv_kwp,
            "module_power_wp": module_power_wp,
            "recommended_modules_count": modules_count
        },
        "string_configuration": string_config,
        "inverter_analysis": inverter_analysis,
        "battery_analysis": {
            "required_battery_capacity_kwh": required_battery_capacity,
            "installed_battery_capacity_kwh": battery_capacity_kwh,
            "actual_autonomy_hours": actual_battery_autonomy,
            "depth_of_discharge": depth_of_discharge,
            "battery_efficiency": battery_efficiency
        },
        "system_type": system_type,
        "has_generator_backup": has_generator_backup,
        "recommendations": recommendations
    }
