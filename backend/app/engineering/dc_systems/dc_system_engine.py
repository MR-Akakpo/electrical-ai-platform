def calculate_dc_load_current(
    dc_power_w: float,
    dc_voltage_v: float
):

    current = (
        dc_power_w
        / dc_voltage_v
    )

    return round(current, 2)


def calculate_battery_autonomy(
    battery_capacity_ah: float,
    dc_load_current_a: float,
    battery_derating_factor: float = 0.8
):

    autonomy_h = (
        battery_capacity_ah
        * battery_derating_factor
    ) / dc_load_current_a

    return round(
        autonomy_h,
        2
    )


def recommend_dc_protection(
    dc_voltage_v: float,
    dc_current_a: float
):

    recommendations = []

    recommendations.append(
        "Use DC-rated protective devices."
    )

    if dc_voltage_v >= 110:

        recommendations.append(
            "High DC voltage detected. Verify DC arc interruption capability carefully."
        )

    if dc_current_a >= 100:

        recommendations.append(
            "High DC current detected. Verify thermal rise and cable sizing."
        )

    return recommendations


def evaluate_rectifier_redundancy(
    total_required_current_a: float,
    rectifier_module_current_a: float
):

    modules_required = (
        total_required_current_a
        / rectifier_module_current_a
    )

    modules_required = int(modules_required) + 1

    n_plus_1_modules = (
        modules_required + 1
    )

    return {
        "minimum_modules_required": modules_required,
        "recommended_n_plus_1_modules": n_plus_1_modules
    }


def run_dc_system_analysis(
    dc_voltage_v: float,
    dc_power_w: float,
    battery_capacity_ah: float,
    rectifier_module_current_a: float
):

    load_current = (
        calculate_dc_load_current(
            dc_power_w=dc_power_w,
            dc_voltage_v=dc_voltage_v
        )
    )

    autonomy = (
        calculate_battery_autonomy(
            battery_capacity_ah=battery_capacity_ah,
            dc_load_current_a=load_current
        )
    )

    protection = (
        recommend_dc_protection(
            dc_voltage_v=dc_voltage_v,
            dc_current_a=load_current
        )
    )

    redundancy = (
        evaluate_rectifier_redundancy(
            total_required_current_a=load_current,
            rectifier_module_current_a=rectifier_module_current_a
        )
    )

    recommendations = []

    recommendations.extend(protection)

    recommendations.append(
        "Verify float/boost charging strategy and battery temperature compensation."
    )

    recommendations.append(
        "Verify telecom/substation DC distribution selectivity and polarity."
    )

    return {
        "dc_voltage_v": dc_voltage_v,
        "dc_load_current_a": load_current,
        "battery_autonomy_hours": autonomy,
        "rectifier_redundancy": redundancy,
        "recommendations": recommendations
    }
