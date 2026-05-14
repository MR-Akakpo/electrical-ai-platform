def calculate_motor_current(
    motor_power_kw: float,
    voltage_v: float,
    efficiency: float,
    power_factor: float,
    phase: str = "three"
):

    if phase == "three":

        current = (
            motor_power_kw * 1000
        ) / (
            1.732
            * voltage_v
            * efficiency
            * power_factor
        )

    else:

        current = (
            motor_power_kw * 1000
        ) / (
            voltage_v
            * efficiency
            * power_factor
        )

    return round(current, 2)


def estimate_motor_starting_current(
    full_load_current_a: float,
    starting_method: str
):

    starting_method = starting_method.lower()

    multiplier = 6

    if "star" in starting_method:
        multiplier = 2

    elif "soft" in starting_method:
        multiplier = 3

    elif "vfd" in starting_method:
        multiplier = 1.2

    starting_current = (
        full_load_current_a
        * multiplier
    )

    return round(starting_current, 2)


def evaluate_motor_loading(
    motor_power_kw: float,
    connected_load_kw: float
):

    loading_percent = (
        connected_load_kw
        / motor_power_kw
    ) * 100

    status = "acceptable"

    recommendations = []

    if loading_percent > 100:

        status = "overloaded"

        recommendations.append(
            "Motor overloaded."
        )

    elif loading_percent > 90:

        status = "high"

        recommendations.append(
            "Motor heavily loaded. Verify thermal limits."
        )

    elif loading_percent < 40:

        status = "low"

        recommendations.append(
            "Motor lightly loaded. Verify sizing optimization."
        )

    else:

        recommendations.append(
            "Motor loading appears acceptable."
        )

    return {
        "status": status,
        "loading_percent": round(loading_percent, 2),
        "recommendations": recommendations
    }


def recommend_motor_protection(
    motor_power_kw: float,
    starting_method: str,
    criticality: str
):

    recommendations = []

    recommendations.append(
        "Thermal overload protection required."
    )

    recommendations.append(
        "Short-circuit protection required."
    )

    if motor_power_kw > 55:

        recommendations.append(
            "Large motor detected. Ground fault and phase imbalance protection recommended."
        )

    if "vfd" in starting_method.lower():

        recommendations.append(
            "VFD detected. Verify harmonic mitigation and motor insulation compatibility."
        )

    if criticality.lower() == "critical":

        recommendations.append(
            "Critical motor application detected. Consider redundancy and predictive maintenance."
        )

    return recommendations


def run_motor_analysis(
    motor_power_kw: float,
    voltage_v: float,
    efficiency: float,
    power_factor: float,
    connected_load_kw: float,
    starting_method: str,
    criticality: str,
    application: str
):

    full_load_current = calculate_motor_current(
        motor_power_kw=motor_power_kw,
        voltage_v=voltage_v,
        efficiency=efficiency,
        power_factor=power_factor
    )

    starting_current = estimate_motor_starting_current(
        full_load_current_a=full_load_current,
        starting_method=starting_method
    )

    loading = evaluate_motor_loading(
        motor_power_kw=motor_power_kw,
        connected_load_kw=connected_load_kw
    )

    protection = recommend_motor_protection(
        motor_power_kw=motor_power_kw,
        starting_method=starting_method,
        criticality=criticality
    )

    recommendations = []

    recommendations.extend(
        loading["recommendations"]
    )

    recommendations.extend(
        protection
    )

    if application.lower() == "hvac":

        recommendations.append(
            "HVAC application detected. Verify variable torque profile."
        )

    if application.lower() == "pump":

        recommendations.append(
            "Pump application detected. Verify dry-run and cavitation protection."
        )

    recommendations.append(
        "Verify cable sizing, voltage drop and coordination with upstream protection."
    )

    return {
        "motor_power_kw": motor_power_kw,
        "full_load_current_a": full_load_current,
        "starting_current_a": starting_current,
        "loading_analysis": loading,
        "recommendations": recommendations
    }
from app.engineering.motors.motor_engine import (
    run_motor_analysis
)


def run_motor_engineering_analysis(
    motor_power_kw: float,
    voltage_v: float,
    power_factor: float,
    efficiency: float,
    starting_method: str,
    generator_kva: float = 0
):

    return run_motor_analysis(
        motor_power_kw=motor_power_kw,
        voltage_v=voltage_v,
        efficiency=efficiency,
        power_factor=power_factor,
        connected_load_kw=motor_power_kw,
        starting_method=starting_method,
        criticality="standard",
        application="general"
    )


from app.engineering.motors.motor_engine import *
