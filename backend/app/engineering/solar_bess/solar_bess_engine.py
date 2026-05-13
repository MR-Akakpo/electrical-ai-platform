def calculate_pv_array_power(
    module_power_wp: float,
    number_of_modules: int,
    performance_ratio: float = 0.8
):

    dc_power_kwp = (
        module_power_wp
        * number_of_modules
    ) / 1000

    expected_ac_power_kw = (
        dc_power_kwp
        * performance_ratio
    )

    return {
        "dc_power_kwp": round(dc_power_kwp, 2),
        "expected_ac_power_kw": round(expected_ac_power_kw, 2)
    }


def calculate_bess_autonomy(
    battery_capacity_kwh: float,
    load_kw: float,
    depth_of_discharge: float = 0.8
):

    usable_energy = (
        battery_capacity_kwh
        * depth_of_discharge
    )

    autonomy_hours = (
        usable_energy
        / load_kw
    )

    return round(autonomy_hours, 2)


def evaluate_inverter_sizing(
    pv_dc_power_kwp: float,
    inverter_ac_power_kw: float
):

    dc_ac_ratio = (
        pv_dc_power_kwp
        / inverter_ac_power_kw
    )

    recommendations = []

    if dc_ac_ratio > 1.35:
        recommendations.append(
            "High DC/AC ratio detected. Verify inverter clipping losses."
        )

    elif dc_ac_ratio < 0.9:
        recommendations.append(
            "Inverter may be oversized compared to PV array."
        )

    else:
        recommendations.append(
            "PV inverter sizing appears within a typical range."
        )

    return {
        "dc_ac_ratio": round(dc_ac_ratio, 2),
        "recommendations": recommendations
    }


def run_solar_bess_analysis(
    module_power_wp: float,
    number_of_modules: int,
    inverter_ac_power_kw: float,
    battery_capacity_kwh: float,
    critical_load_kw: float,
    performance_ratio: float = 0.8,
    depth_of_discharge: float = 0.8
):

    pv_power = calculate_pv_array_power(
        module_power_wp=module_power_wp,
        number_of_modules=number_of_modules,
        performance_ratio=performance_ratio
    )

    bess_autonomy = calculate_bess_autonomy(
        battery_capacity_kwh=battery_capacity_kwh,
        load_kw=critical_load_kw,
        depth_of_discharge=depth_of_discharge
    )

    inverter = evaluate_inverter_sizing(
        pv_dc_power_kwp=pv_power["dc_power_kwp"],
        inverter_ac_power_kw=inverter_ac_power_kw
    )

    recommendations = []

    recommendations.extend(
        inverter["recommendations"]
    )

    recommendations.append(
        "Verify DC protection, string fusing, surge protection, earthing and inverter anti-islanding."
    )

    recommendations.append(
        "For hybrid systems, verify generator/PV/BESS coordination and load priority."
    )

    return {
        "pv_power": pv_power,
        "inverter_analysis": inverter,
        "battery_autonomy_hours": bess_autonomy,
        "recommendations": recommendations
    }
