def calculate_transformer_full_load_current(
    transformer_power_kva: float,
    voltage_v: float,
    phase: str = "three"
):

    if phase == "three":

        current = (
            transformer_power_kva * 1000
        ) / (
            1.732 * voltage_v
        )

    else:

        current = (
            transformer_power_kva * 1000
        ) / voltage_v

    return round(current, 2)


def evaluate_transformer_loading(
    transformer_power_kva: float,
    connected_load_kva: float
):

    loading_percent = (
        connected_load_kva
        / transformer_power_kva
    ) * 100

    recommendations = []

    status = "acceptable"

    if loading_percent > 100:

        status = "overloaded"

        recommendations.append(
            "Transformer overloaded. Increase transformer capacity or reduce load."
        )

    elif loading_percent > 80:

        status = "high"

        recommendations.append(
            "Transformer heavily loaded. Verify future expansion and cooling."
        )

    elif loading_percent < 30:

        status = "low"

        recommendations.append(
            "Transformer lightly loaded. Verify economic optimization."
        )

    else:

        recommendations.append(
            "Transformer loading appears acceptable."
        )

    return {
        "loading_percent": round(loading_percent, 2),
        "status": status,
        "recommendations": recommendations
    }


def evaluate_transformer_efficiency(
    no_load_losses_kw: float,
    load_losses_kw: float,
    connected_load_kva: float,
    power_factor: float
):

    output_power_kw = (
        connected_load_kva
        * power_factor
    )

    total_losses = (
        no_load_losses_kw
        + load_losses_kw
    )

    efficiency = (
        output_power_kw
        /
        (
            output_power_kw + total_losses
        )
    ) * 100

    return round(efficiency, 2)


def evaluate_parallel_operation(
    impedance_percent: float,
    second_transformer_impedance_percent: float,
    vector_group: str,
    second_vector_group: str
):

    recommendations = []

    compatible = True

    if vector_group != second_vector_group:

        compatible = False

        recommendations.append(
            "Transformer vector groups are incompatible for parallel operation."
        )

    impedance_difference = abs(
        impedance_percent
        - second_transformer_impedance_percent
    )

    if impedance_difference > 0.5:

        compatible = False

        recommendations.append(
            "Transformer impedances differ significantly. Load sharing may be poor."
        )

    if compatible:

        recommendations.append(
            "Transformers appear compatible for parallel operation."
        )

    return {
        "compatible": compatible,
        "recommendations": recommendations
    }


def run_transformer_analysis(
    transformer_power_kva: float,
    primary_voltage_v: float,
    secondary_voltage_v: float,
    connected_load_kva: float,
    power_factor: float,
    impedance_percent: float,
    vector_group: str,
    cooling_mode: str,
    no_load_losses_kw: float,
    load_losses_kw: float,
    parallel_operation_required: bool = False,
    second_transformer_impedance_percent: float = 6,
    second_vector_group: str = "Dyn11"
):

    primary_current = calculate_transformer_full_load_current(
        transformer_power_kva=transformer_power_kva,
        voltage_v=primary_voltage_v
    )

    secondary_current = calculate_transformer_full_load_current(
        transformer_power_kva=transformer_power_kva,
        voltage_v=secondary_voltage_v
    )

    loading = evaluate_transformer_loading(
        transformer_power_kva=transformer_power_kva,
        connected_load_kva=connected_load_kva
    )

    efficiency = evaluate_transformer_efficiency(
        no_load_losses_kw=no_load_losses_kw,
        load_losses_kw=load_losses_kw,
        connected_load_kva=connected_load_kva,
        power_factor=power_factor
    )

    recommendations = []

    recommendations.extend(
        loading["recommendations"]
    )

    if cooling_mode.upper() == "ONAN":

        recommendations.append(
            "ONAN cooling detected. Verify ambient temperature and overload capability."
        )

    if cooling_mode.upper() == "ONAF":

        recommendations.append(
            "ONAF cooling detected. Verify fan redundancy and auxiliary supply."
        )

    parallel_analysis = None

    if parallel_operation_required:

        parallel_analysis = evaluate_parallel_operation(
            impedance_percent=impedance_percent,
            second_transformer_impedance_percent=second_transformer_impedance_percent,
            vector_group=vector_group,
            second_vector_group=second_vector_group
        )

        recommendations.extend(
            parallel_analysis["recommendations"]
        )

    recommendations.append(
        "Verify transformer protection, earthing, inrush current and short-circuit withstand."
    )

    return {
        "transformer_power_kva": transformer_power_kva,
        "primary_voltage_v": primary_voltage_v,
        "secondary_voltage_v": secondary_voltage_v,
        "primary_current_a": primary_current,
        "secondary_current_a": secondary_current,
        "loading_analysis": loading,
        "efficiency_percent": efficiency,
        "vector_group": vector_group,
        "cooling_mode": cooling_mode,
        "parallel_operation_analysis": parallel_analysis,
        "recommendations": recommendations
    }
