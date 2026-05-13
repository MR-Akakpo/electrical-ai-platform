from app.engineering.generators.load_analysis import (
    calculate_generator_required_capacity,
    evaluate_load_type
)

from app.engineering.generators.transient_engine import (
    calculate_voltage_dip,
    transient_recovery_analysis
)

from app.engineering.generators.autonomy_engine import (
    calculate_fuel_autonomy_hours
)

from app.engineering.generators.recommendation_engine import (
    generate_generator_recommendations
)


def run_generator_engineering_analysis(
    total_load_kw: float,
    power_factor: float,
    motor_start_kva: float,
    fuel_tank_liters: float,
    fuel_consumption_lph: float,
    load_type: str = "mixed",
    redundancy_type: str = "N+1"
):

    required_kva = (
        calculate_generator_required_capacity(
            total_load_kw=total_load_kw,
            power_factor=power_factor
        )
    )

    load_analysis = evaluate_load_type(
        load_type
    )

    adjusted_generator_kva = (
        required_kva
        * load_analysis["oversizing_factor"]
    )

    voltage_dip = (
        calculate_voltage_dip(
            generator_kva=adjusted_generator_kva,
            motor_start_kva=motor_start_kva
        )
    )

    transient_analysis = (
        transient_recovery_analysis(
            voltage_dip_percent=voltage_dip
        )
    )

    autonomy = (
        calculate_fuel_autonomy_hours(
            fuel_tank_liters=fuel_tank_liters,
            fuel_consumption_lph=fuel_consumption_lph
        )
    )

    recommendations = (
        generate_generator_recommendations(
            voltage_dip_percent=voltage_dip,
            autonomy_hours=autonomy,
            redundancy_type=redundancy_type
        )
    )

    return {

        "required_generator_kva":
            round(adjusted_generator_kva, 2),

        "base_generator_kva":
            required_kva,

        "load_analysis":
            load_analysis,

        "voltage_dip_percent":
            voltage_dip,

        "transient_analysis":
            transient_analysis,

        "fuel_autonomy_hours":
            autonomy,

        "redundancy_type":
            redundancy_type,

        "recommendations":
            recommendations
    }
