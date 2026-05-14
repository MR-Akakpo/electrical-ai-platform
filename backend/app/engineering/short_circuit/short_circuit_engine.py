def calculate_transformer_impedance_ohm(
    transformer_power_kva: float,
    voltage_v: float,
    impedance_percent: float
):

    z = (
        (
            voltage_v ** 2
        )
        /
        (
            transformer_power_kva * 1000
        )
    ) * (
        impedance_percent / 100
    )

    return z


def calculate_three_phase_short_circuit_current(
    voltage_v: float,
    impedance_ohm: float
):

    ik3 = (
        voltage_v
        /
        (
            1.732 * impedance_ohm
        )
    )

    return round(
        ik3 / 1000,
        2
    )


def estimate_peak_short_circuit_current(
    ik3_ka: float,
    xr_ratio: float
):

    factor = 1.02 + (
        0.98 * (2.718 ** (-3 / xr_ratio))
    )

    ip = (
        factor
        * 1.414
        * ik3_ka
    )

    return round(ip, 2)


def evaluate_breaking_capacity(
    short_circuit_current_ka: float,
    breaker_capacity_ka: float
):

    compliant = (
        breaker_capacity_ka
        >= short_circuit_current_ka
    )

    recommendations = []

    if compliant:

        recommendations.append(
            "Breaking capacity appears acceptable."
        )

    else:

        recommendations.append(
            "Breaking capacity insufficient for calculated fault current."
        )

    return {
        "compliant": compliant,
        "recommendations": recommendations
    }


def evaluate_thermal_withstand(
    short_circuit_current_ka: float,
    duration_s: float
):

    thermal_stress = (
        short_circuit_current_ka ** 2
    ) * duration_s

    return round(thermal_stress, 2)


def run_short_circuit_analysis(
    transformer_power_kva: float,
    voltage_v: float,
    impedance_percent: float,
    xr_ratio: float,
    breaker_capacity_ka: float,
    fault_duration_s: float
):

    impedance = calculate_transformer_impedance_ohm(
        transformer_power_kva=transformer_power_kva,
        voltage_v=voltage_v,
        impedance_percent=impedance_percent
    )

    ik3 = calculate_three_phase_short_circuit_current(
        voltage_v=voltage_v,
        impedance_ohm=impedance
    )

    peak = estimate_peak_short_circuit_current(
        ik3_ka=ik3,
        xr_ratio=xr_ratio
    )

    breaking = evaluate_breaking_capacity(
        short_circuit_current_ka=ik3,
        breaker_capacity_ka=breaker_capacity_ka
    )

    thermal = evaluate_thermal_withstand(
        short_circuit_current_ka=ik3,
        duration_s=fault_duration_s
    )

    recommendations = []

    recommendations.extend(
        breaking["recommendations"]
    )

    recommendations.append(
        "Verify busbar, cable and switchgear short-time withstand ratings."
    )

    recommendations.append(
        "Verify protection selectivity and arc flash impact."
    )

    return {
        "transformer_impedance_ohm": round(impedance, 6),
        "three_phase_short_circuit_ka": ik3,
        "peak_short_circuit_ka": peak,
        "thermal_stress_kA2s": thermal,
        "breaking_capacity_analysis": breaking,
        "recommendations": recommendations
    }
