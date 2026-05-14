def calculate_generator_current(
    generator_power_kva: float,
    voltage_v: float,
    phase: str = "three"
):

    if phase == "three":

        current = (
            generator_power_kva * 1000
        ) / (
            1.732 * voltage_v
        )

    else:

        current = (
            generator_power_kva * 1000
        ) / voltage_v

    return round(current, 2)


def evaluate_generator_loading(
    generator_power_kva: float,
    connected_load_kva: float
):

    loading_percent = (
        connected_load_kva
        / generator_power_kva
    ) * 100

    status = "acceptable"

    recommendations = []

    if loading_percent > 100:

        status = "overloaded"

        recommendations.append(
            "Generator overloaded. Increase generator capacity or reduce load."
        )

    elif loading_percent > 80:

        status = "high"

        recommendations.append(
            "Generator heavily loaded. Verify transient motor starting and future expansion."
        )

    elif loading_percent < 30:

        status = "low"

        recommendations.append(
            "Generator lightly loaded. Wet stacking risk may exist for diesel generators."
        )

    else:

        recommendations.append(
            "Generator loading appears acceptable."
        )

    return {
        "loading_percent": round(loading_percent, 2),
        "status": status,
        "recommendations": recommendations
    }


def evaluate_motor_starting_impact(
    largest_motor_kw: float,
    generator_power_kva: float
):

    ratio = (
        largest_motor_kw
        / generator_power_kva
    ) * 100

    recommendations = []

    if ratio > 30:

        recommendations.append(
            "Large motor starting impact detected. Verify voltage dip and transient response."
        )

    else:

        recommendations.append(
            "Motor starting impact appears acceptable."
        )

    return {
        "largest_motor_to_generator_ratio_percent": round(ratio, 2),
        "recommendations": recommendations
    }


def evaluate_fuel_autonomy(
    fuel_tank_liters: float,
    fuel_consumption_lph: float
):

    autonomy_hours = (
        fuel_tank_liters
        / fuel_consumption_lph
    )

    return round(autonomy_hours, 2)


def evaluate_redundancy(
    number_of_generators: int,
    required_generators: int
):

    recommendations = []

    if number_of_generators > required_generators:

        recommendations.append(
            "Generator redundancy detected (N+1 or higher)."
        )

    elif number_of_generators == required_generators:

        recommendations.append(
            "No generator redundancy available."
        )

    else:

        recommendations.append(
            "Insufficient generator quantity for required load."
        )

    return recommendations


def run_generator_analysis(
    generator_power_kva: float,
    voltage_v: float,
    connected_load_kva: float,
    largest_motor_kw: float,
    fuel_tank_liters: float,
    fuel_consumption_lph: float,
    number_of_generators: int,
    required_generators: int,
    application: str,
    generator_type: str = "diesel"
):

    current = calculate_generator_current(
        generator_power_kva=generator_power_kva,
        voltage_v=voltage_v
    )

    loading = evaluate_generator_loading(
        generator_power_kva=generator_power_kva,
        connected_load_kva=connected_load_kva
    )

    motor = evaluate_motor_starting_impact(
        largest_motor_kw=largest_motor_kw,
        generator_power_kva=generator_power_kva
    )

    autonomy = evaluate_fuel_autonomy(
        fuel_tank_liters=fuel_tank_liters,
        fuel_consumption_lph=fuel_consumption_lph
    )

    redundancy = evaluate_redundancy(
        number_of_generators=number_of_generators,
        required_generators=required_generators
    )

    recommendations = []

    recommendations.extend(
        loading["recommendations"]
    )

    recommendations.extend(
        motor["recommendations"]
    )

    recommendations.extend(
        redundancy
    )

    if application.lower() == "data_center":

        recommendations.append(
            "Data center application detected. Verify black-start strategy, synchronization and UPS coordination."
        )

    if generator_type.lower() == "diesel":

        recommendations.append(
            "Verify fuel polishing, fuel redundancy and exhaust ventilation."
        )

    recommendations.append(
        "Verify short-circuit contribution, protection coordination and grounding philosophy."
    )

    return {
        "generator_power_kva": generator_power_kva,
        "generator_current_a": current,
        "loading_analysis": loading,
        "motor_starting_analysis": motor,
        "fuel_autonomy_hours": autonomy,
        "recommendations": recommendations
    }
