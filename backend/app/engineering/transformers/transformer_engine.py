def calculate_transformer_full_load_current(
    transformer_kva: float,
    voltage_v: float,
    phase: str = "three"
):

    if phase == "three":

        current = (
            transformer_kva * 1000
        ) / (
            1.732 * voltage_v
        )

    else:

        current = (
            transformer_kva * 1000
        ) / voltage_v

    return round(current, 2)


def calculate_transformer_short_circuit_current(
    transformer_kva: float,
    voltage_v: float,
    impedance_percent: float,
    phase: str = "three"
):

    full_load_current = calculate_transformer_full_load_current(
        transformer_kva=transformer_kva,
        voltage_v=voltage_v,
        phase=phase
    )

    if impedance_percent <= 0:

        return 0

    ik = (
        full_load_current
        * 100
        / impedance_percent
    )

    return round(ik, 2)


def analyze_transformer_loading(
    transformer_kva: float,
    connected_load_kw: float,
    power_factor: float
):

    apparent_load_kva = (
        connected_load_kw
        / power_factor
    )

    loading_percent = (
        apparent_load_kva
        / transformer_kva
    ) * 100

    recommendations = []

    if loading_percent > 100:

        recommendations.append(
            "Transformer overloaded. Increase transformer rating or reduce connected load."
        )

    elif loading_percent > 80:

        recommendations.append(
            "Transformer loading is high. Consider future expansion margin."
        )

    elif loading_percent < 30:

        recommendations.append(
            "Transformer is lightly loaded. Verify efficiency and economic sizing."
        )

    else:

        recommendations.append(
            "Transformer loading is within a normal operating range."
        )

    return {
        "apparent_load_kva": round(apparent_load_kva, 2),
        "loading_percent": round(loading_percent, 2),
        "recommendations": recommendations
    }


def run_transformer_analysis(
    transformer_kva: float,
    primary_voltage_v: float,
    secondary_voltage_v: float,
    impedance_percent: float,
    connected_load_kw: float,
    power_factor: float,
    phase: str = "three"
):

    primary_current = calculate_transformer_full_load_current(
        transformer_kva=transformer_kva,
        voltage_v=primary_voltage_v,
        phase=phase
    )

    secondary_current = calculate_transformer_full_load_current(
        transformer_kva=transformer_kva,
        voltage_v=secondary_voltage_v,
        phase=phase
    )

    secondary_short_circuit_current = calculate_transformer_short_circuit_current(
        transformer_kva=transformer_kva,
        voltage_v=secondary_voltage_v,
        impedance_percent=impedance_percent,
        phase=phase
    )

    loading = analyze_transformer_loading(
        transformer_kva=transformer_kva,
        connected_load_kw=connected_load_kw,
        power_factor=power_factor
    )

    return {
        "transformer_kva": transformer_kva,
        "primary_voltage_v": primary_voltage_v,
        "secondary_voltage_v": secondary_voltage_v,
        "impedance_percent": impedance_percent,
        "primary_full_load_current_a": primary_current,
        "secondary_full_load_current_a": secondary_current,
        "secondary_short_circuit_current_a": secondary_short_circuit_current,
        "loading_analysis": loading
    }
