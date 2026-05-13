def calculate_required_luminous_flux(
    area_m2: float,
    target_lux: float,
    maintenance_factor: float = 0.8,
    utilization_factor: float = 0.6
):

    flux_lm = (
        area_m2
        * target_lux
    ) / (
        maintenance_factor
        * utilization_factor
    )

    return round(flux_lm, 2)


def estimate_lighting_power(
    luminous_flux_lm: float,
    luminaire_efficiency_lm_w: float
):

    power_w = (
        luminous_flux_lm
        / luminaire_efficiency_lm_w
    )

    return round(power_w, 2)


def analyze_lighting_installation(
    area_m2: float,
    target_lux: float,
    luminaire_efficiency_lm_w: float,
    maintenance_factor: float = 0.8,
    utilization_factor: float = 0.6,
    emergency_lighting_required: bool = False
):

    flux = calculate_required_luminous_flux(
        area_m2=area_m2,
        target_lux=target_lux,
        maintenance_factor=maintenance_factor,
        utilization_factor=utilization_factor
    )

    power_w = estimate_lighting_power(
        luminous_flux_lm=flux,
        luminaire_efficiency_lm_w=luminaire_efficiency_lm_w
    )

    power_density_w_m2 = (
        power_w
        / area_m2
    )

    recommendations = []

    if power_density_w_m2 > 15:
        recommendations.append(
            "High lighting power density detected. Consider higher-efficiency luminaires or lighting zoning."
        )

    if emergency_lighting_required:
        recommendations.append(
            "Emergency lighting required. Provide dedicated emergency circuits or autonomous emergency luminaires."
        )

    recommendations.append(
        "Verify lighting uniformity, glare control, emergency lighting and circuit voltage drop."
    )

    return {
        "required_luminous_flux_lm": flux,
        "estimated_lighting_power_w": power_w,
        "power_density_w_m2": round(power_density_w_m2, 2),
        "target_lux": target_lux,
        "recommendations": recommendations
    }
