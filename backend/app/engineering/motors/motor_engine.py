from app.engineering.motors.motor_sizing import (
    calculate_motor_full_load_current
)

from app.engineering.motors.starting_analysis import (
    calculate_motor_starting_current
)

from app.engineering.motors.generator_impact import (
    evaluate_generator_motor_impact
)

from app.engineering.motors.protection_selection import (
    recommend_motor_protection
)

from app.engineering.motors.cable_recommendations import (
    recommend_motor_cable_strategy
)


def run_motor_engineering_analysis(
    motor_power_kw: float,
    voltage_v: float,
    power_factor: float,
    efficiency: float,
    starting_method: str,
    generator_kva: float
):

    full_load_current = (
        calculate_motor_full_load_current(
            motor_power_kw=motor_power_kw,
            voltage_v=voltage_v,
            power_factor=power_factor,
            efficiency=efficiency
        )
    )

    starting_analysis = (
        calculate_motor_starting_current(
            full_load_current_a=full_load_current,
            starting_method=starting_method
        )
    )

    motor_starting_kva = (
        1.732
        * voltage_v
        * starting_analysis["starting_current_a"]
    ) / 1000

    generator_impact = (
        evaluate_generator_motor_impact(
            generator_kva=generator_kva,
            motor_starting_kva=motor_starting_kva
        )
    )

    protection = (
        recommend_motor_protection(
            motor_current_a=full_load_current,
            starting_method=starting_method
        )
    )

    cable_strategy = (
        recommend_motor_cable_strategy(
            motor_power_kw=motor_power_kw,
            starting_method=starting_method
        )
    )

    recommendations = []

    recommendations.extend(
        generator_impact["recommendations"]
    )

    recommendations.extend(
        protection
    )

    recommendations.extend(
        cable_strategy
    )

    return {

        "motor_power_kw":
            motor_power_kw,

        "full_load_current_a":
            full_load_current,

        "starting_analysis":
            starting_analysis,

        "motor_starting_kva":
            round(
                motor_starting_kva,
                2
            ),

        "generator_impact":
            generator_impact,

        "recommendations":
            recommendations
    }
