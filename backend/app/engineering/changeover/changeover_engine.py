def determine_changeover_type(
    application: str,
    criticality: str,
    transfer_time_requirement_s: float
):

    application = application.lower()
    criticality = criticality.lower()

    if transfer_time_requirement_s <= 0.02:
        return "STS - Static Transfer Switch"

    if criticality == "critical" or "data_center" in application:
        return "Automatic Transfer Switch with bypass/maintenance arrangement"

    return "Automatic Transfer Switch"


def analyze_transfer_time(
    transfer_time_s: float,
    load_type: str
):

    recommendations = []

    acceptable = True

    load_type = load_type.lower()

    if load_type in ["ups", "data_center", "critical"] and transfer_time_s > 0.1:
        acceptable = False
        recommendations.append(
            "Transfer time may be too long for critical loads. Consider UPS ride-through or STS."
        )

    elif transfer_time_s > 10:
        recommendations.append(
            "Long transfer time detected. Verify process continuity requirements."
        )

    else:
        recommendations.append(
            "Transfer time appears acceptable for preliminary assessment."
        )

    return {
        "acceptable": acceptable,
        "transfer_time_s": transfer_time_s,
        "recommendations": recommendations
    }


def analyze_interlocking_requirements(
    source_1_type: str,
    source_2_type: str,
    closed_transition: bool
):

    recommendations = []

    if closed_transition:
        recommendations.append(
            "Closed transition selected. Verify synchronization, voltage, frequency and phase angle matching."
        )
    else:
        recommendations.append(
            "Open transition selected. Verify load tolerance to interruption."
        )

    if "generator" in source_1_type.lower() or "generator" in source_2_type.lower():
        recommendations.append(
            "Generator source detected. Verify start signal, warm-up time, cooldown time and return-to-utility logic."
        )

    recommendations.append(
        "Mechanical and electrical interlocking are required to prevent source paralleling when not intended."
    )

    return recommendations


def run_changeover_analysis(
    application: str,
    source_1_type: str,
    source_2_type: str,
    rated_current_a: float,
    load_type: str,
    criticality: str,
    transfer_time_s: float,
    closed_transition: bool
):

    changeover_type = determine_changeover_type(
        application=application,
        criticality=criticality,
        transfer_time_requirement_s=transfer_time_s
    )

    transfer = analyze_transfer_time(
        transfer_time_s=transfer_time_s,
        load_type=load_type
    )

    interlocking = analyze_interlocking_requirements(
        source_1_type=source_1_type,
        source_2_type=source_2_type,
        closed_transition=closed_transition
    )

    recommendations = []

    recommendations.extend(transfer["recommendations"])
    recommendations.extend(interlocking)

    if rated_current_a >= 1600:
        recommendations.append(
            "High-current changeover detected. Verify short-time withstand, busbar rating and maintenance bypass."
        )

    return {
        "recommended_changeover_type": changeover_type,
        "source_1_type": source_1_type,
        "source_2_type": source_2_type,
        "rated_current_a": rated_current_a,
        "transfer_analysis": transfer,
        "closed_transition": closed_transition,
        "recommendations": recommendations
    }
