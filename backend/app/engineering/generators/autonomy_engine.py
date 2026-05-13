def calculate_fuel_autonomy_hours(
    fuel_tank_liters: float,
    fuel_consumption_lph: float
):

    if fuel_consumption_lph <= 0:

        return 0

    autonomy = (
        fuel_tank_liters
        / fuel_consumption_lph
    )

    return round(
        autonomy,
        2
    )
