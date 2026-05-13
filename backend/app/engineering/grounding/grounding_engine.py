def analyze_earthing_system(
    earthing_system: str,
    fault_current_a: float,
    earth_resistance_ohm: float,
    touch_voltage_limit_v: float = 50
):

    earthing_system = earthing_system.upper()

    touch_voltage = (
        fault_current_a
        * earth_resistance_ohm
    )

    compliant = touch_voltage <= touch_voltage_limit_v

    recommendations = []

    if earthing_system == "TT":

        recommendations.append(
            "TT earthing system detected. RCD protection is generally required because earth fault current may be limited by earth resistance."
        )

    elif earthing_system == "IT":

        recommendations.append(
            "IT earthing system detected. Insulation monitoring device is required to detect the first fault."
        )

        recommendations.append(
            "For IT systems, verify second-fault protection and continuity of service requirements."
        )

    elif earthing_system == "TN-S":

        recommendations.append(
            "TN-S earthing system detected. Neutral and protective conductor are separated throughout the installation."
        )

        recommendations.append(
            "Verify PE continuity, fault loop impedance and automatic disconnection time."
        )

    elif earthing_system == "TN-C":

        recommendations.append(
            "TN-C earthing system detected. PEN conductor is used. Verify PEN continuity and minimum conductor section requirements."
        )

        recommendations.append(
            "RCD protection is generally not compatible downstream of TN-C sections unless PEN is separated first."
        )

    elif earthing_system == "TN-C-S":

        recommendations.append(
            "TN-C-S earthing system detected. PEN conductor is used upstream and separated into PE and N downstream."
        )

        recommendations.append(
            "Verify PEN separation point, bonding, PE continuity and downstream RCD compatibility."
        )

    else:

        recommendations.append(
            "Unknown earthing system. Use TT, IT, TN-S, TN-C or TN-C-S."
        )

    if not compliant:

        recommendations.append(
            "Touch voltage exceeds safety limit. Improve earthing resistance, verify protective device operation or reduce disconnection time."
        )

    return {
        "earthing_system": earthing_system,
        "fault_current_a": fault_current_a,
        "earth_resistance_ohm": earth_resistance_ohm,
        "touch_voltage_v": round(touch_voltage, 2),
        "touch_voltage_limit_v": touch_voltage_limit_v,
        "compliant": compliant,
        "recommendations": recommendations
    }
