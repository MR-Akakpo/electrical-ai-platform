def estimate_busbar_current_density(
    rated_current_a: float,
    busbar_section_mm2: float
):

    current_density = (
        rated_current_a
        / busbar_section_mm2
    )

    return round(current_density, 3)


def evaluate_busbar_current_density(
    current_density_a_mm2: float,
    material: str
):

    material = material.lower()

    limit = 1.6

    if material == "aluminum":

        limit = 1.2

    status = "acceptable"

    recommendations = []

    if current_density_a_mm2 > limit:

        status = "high"

        recommendations.append(
            "Busbar current density is high. Increase busbar section or improve ventilation."
        )

    else:

        recommendations.append(
            "Busbar current density appears acceptable for preliminary sizing."
        )

    return {
        "status": status,
        "limit_a_mm2": limit,
        "recommendations": recommendations
    }


def evaluate_busbar_short_time_withstand(
    short_circuit_current_ka: float,
    withstand_current_ka: float,
    duration_s: float
):

    compliant = withstand_current_ka >= short_circuit_current_ka

    recommendations = []

    if not compliant:

        recommendations.append(
            "Busbar short-time withstand is insufficient. Increase busbar rating or reduce fault level."
        )

    else:

        recommendations.append(
            "Busbar short-time withstand appears acceptable."
        )

    return {
        "short_circuit_current_ka": short_circuit_current_ka,
        "withstand_current_ka": withstand_current_ka,
        "duration_s": duration_s,
        "compliant": compliant,
        "recommendations": recommendations
    }


def evaluate_busbar_peak_withstand(
    peak_fault_current_ka: float,
    peak_withstand_ka: float
):

    compliant = peak_withstand_ka >= peak_fault_current_ka

    recommendations = []

    if not compliant:

        recommendations.append(
            "Busbar peak withstand is insufficient. Verify electrodynamic forces and support spacing."
        )

    else:

        recommendations.append(
            "Busbar peak withstand appears acceptable."
        )

    return {
        "peak_fault_current_ka": peak_fault_current_ka,
        "peak_withstand_ka": peak_withstand_ka,
        "compliant": compliant,
        "recommendations": recommendations
    }


def run_busbar_analysis(
    rated_current_a: float,
    busbar_section_mm2: float,
    material: str,
    short_circuit_current_ka: float,
    withstand_current_ka: float,
    peak_fault_current_ka: float,
    peak_withstand_ka: float,
    duration_s: float
):

    current_density = estimate_busbar_current_density(
        rated_current_a=rated_current_a,
        busbar_section_mm2=busbar_section_mm2
    )

    density_analysis = evaluate_busbar_current_density(
        current_density_a_mm2=current_density,
        material=material
    )

    short_time = evaluate_busbar_short_time_withstand(
        short_circuit_current_ka=short_circuit_current_ka,
        withstand_current_ka=withstand_current_ka,
        duration_s=duration_s
    )

    peak = evaluate_busbar_peak_withstand(
        peak_fault_current_ka=peak_fault_current_ka,
        peak_withstand_ka=peak_withstand_ka
    )

    recommendations = []

    recommendations.extend(density_analysis["recommendations"])
    recommendations.extend(short_time["recommendations"])
    recommendations.extend(peak["recommendations"])

    recommendations.append(
        "Verify temperature rise, enclosure derating, busbar support spacing and manufacturer-certified assembly data."
    )

    return {
        "rated_current_a": rated_current_a,
        "busbar_section_mm2": busbar_section_mm2,
        "material": material,
        "current_density_a_mm2": current_density,
        "current_density_analysis": density_analysis,
        "short_time_withstand_analysis": short_time,
        "peak_withstand_analysis": peak,
        "recommendations": recommendations
    }
