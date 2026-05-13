def determine_switchboard_type(
    application: str,
    rated_current_a: float,
    criticality: str
):

    application = application.lower()
    criticality = criticality.lower()

    if "data_center" in application or criticality == "critical":

        return "Critical LV switchboard / PDU / MDB"

    if rated_current_a >= 1600:

        return "Main LV switchboard / TGBT"

    if rated_current_a >= 400:

        return "Sub-main distribution board"

    return "Distribution board"


def recommend_form_of_separation(
    criticality: str,
    maintenance_requirement: str
):

    criticality = criticality.lower()
    maintenance_requirement = maintenance_requirement.lower()

    if criticality == "critical" or maintenance_requirement == "high":

        return "Form 4 recommended for high availability and safe maintenance."

    if maintenance_requirement == "medium":

        return "Form 3b recommended."

    return "Form 2 or standard internal separation may be acceptable depending on project requirements."


def analyze_busbar_withstand(
    rated_current_a: float,
    short_circuit_level_ka: float,
    duration_s: float
):

    recommendations = []

    if short_circuit_level_ka >= 50:

        recommendations.append(
            "High short-circuit level detected. Verify busbar short-time withstand Icw and peak withstand Ipk."
        )

    if rated_current_a >= 2500:

        recommendations.append(
            "High rated current detected. Verify busbar thermal rise, ventilation and enclosure derating."
        )

    return {
        "rated_current_a": rated_current_a,
        "short_circuit_level_ka": short_circuit_level_ka,
        "duration_s": duration_s,
        "recommendations": recommendations
    }


def recommend_enclosure_protection(
    environment: str
):

    environment = environment.lower()

    if environment == "outdoor":

        return {
            "ip_rating": "IP55 minimum recommended",
            "notes": "Outdoor installation requires weather protection and UV-resistant enclosure."
        }

    if environment in ["industrial", "dusty"]:

        return {
            "ip_rating": "IP54 recommended",
            "notes": "Industrial environment requires dust protection and robust enclosure."
        }

    if environment == "data_center":

        return {
            "ip_rating": "IP31/IP41 typical depending on room cleanliness and airflow design",
            "notes": "Coordinate enclosure protection with cooling, access and maintainability."
        }

    return {
        "ip_rating": "IP31 typical indoor minimum",
        "notes": "Verify project specifications and local standards."
    }


def run_switchboard_analysis(
    application: str,
    rated_current_a: float,
    short_circuit_level_ka: float,
    duration_s: float,
    environment: str,
    criticality: str,
    maintenance_requirement: str
):

    switchboard_type = determine_switchboard_type(
        application=application,
        rated_current_a=rated_current_a,
        criticality=criticality
    )

    form = recommend_form_of_separation(
        criticality=criticality,
        maintenance_requirement=maintenance_requirement
    )

    busbar = analyze_busbar_withstand(
        rated_current_a=rated_current_a,
        short_circuit_level_ka=short_circuit_level_ka,
        duration_s=duration_s
    )

    enclosure = recommend_enclosure_protection(
        environment=environment
    )

    recommendations = []

    recommendations.append(form)

    recommendations.extend(
        busbar["recommendations"]
    )

    recommendations.append(
        enclosure["notes"]
    )

    if criticality.lower() == "critical":

        recommendations.append(
            "Critical switchboard detected. Consider dual incomers, bus coupler, metering, monitoring, selectivity and maintenance bypass strategy."
        )

    return {
        "recommended_switchboard_type": switchboard_type,
        "rated_current_a": rated_current_a,
        "short_circuit_level_ka": short_circuit_level_ka,
        "form_of_separation_recommendation": form,
        "busbar_analysis": busbar,
        "enclosure_recommendation": enclosure,
        "recommendations": recommendations
    }
