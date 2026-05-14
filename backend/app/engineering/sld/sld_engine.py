from uuid import uuid4


def create_node(
    name: str,
    equipment_type: str,
    voltage_v: float,
    power_kva: float | None = None
):

    return {
        "id": str(uuid4()),
        "name": name,
        "equipment_type": equipment_type,
        "voltage_v": voltage_v,
        "power_kva": power_kva,
        "connections": []
    }


def connect_nodes(
    source_node: dict,
    destination_node: dict,
    cable_reference: str | None = None
):

    source_node["connections"].append({
        "destination_id": destination_node["id"],
        "destination_name": destination_node["name"],
        "cable_reference": cable_reference
    })


def build_basic_sld(
    utility_voltage_v: float,
    transformer_power_kva: float,
    generator_power_kva: float,
    ups_power_kva: float,
    main_switchboard_power_kva: float
):

    utility = create_node(
        name="UTILITY",
        equipment_type="UTILITY_SOURCE",
        voltage_v=utility_voltage_v
    )

    transformer = create_node(
        name="TRANSFORMER",
        equipment_type="TRANSFORMER",
        voltage_v=400,
        power_kva=transformer_power_kva
    )

    generator = create_node(
        name="GENERATOR",
        equipment_type="GENERATOR",
        voltage_v=400,
        power_kva=generator_power_kva
    )

    ups = create_node(
        name="UPS",
        equipment_type="UPS",
        voltage_v=400,
        power_kva=ups_power_kva
    )

    main_board = create_node(
        name="TGBT",
        equipment_type="MAIN_SWITCHBOARD",
        voltage_v=400,
        power_kva=main_switchboard_power_kva
    )

    connect_nodes(
        utility,
        transformer,
        "MV_CABLE"
    )

    connect_nodes(
        transformer,
        main_board,
        "LV_MAIN_CABLE"
    )

    connect_nodes(
        generator,
        main_board,
        "GENERATOR_CABLE"
    )

    connect_nodes(
        main_board,
        ups,
        "UPS_FEEDER"
    )

    return {
        "nodes": [
            utility,
            transformer,
            generator,
            main_board,
            ups
        ]
    }


def analyze_sld(
    sld_data: dict
):

    nodes = sld_data.get("nodes", [])

    equipment_summary = {}

    for node in nodes:

        equipment_type = node["equipment_type"]

        equipment_summary[equipment_type] = (
            equipment_summary.get(equipment_type, 0)
            + 1
        )

    return {
        "total_nodes": len(nodes),
        "equipment_summary": equipment_summary
    }


def run_sld_analysis(
    utility_voltage_v: float,
    transformer_power_kva: float,
    generator_power_kva: float,
    ups_power_kva: float,
    main_switchboard_power_kva: float
):

    sld = build_basic_sld(
        utility_voltage_v=utility_voltage_v,
        transformer_power_kva=transformer_power_kva,
        generator_power_kva=generator_power_kva,
        ups_power_kva=ups_power_kva,
        main_switchboard_power_kva=main_switchboard_power_kva
    )

    analysis = analyze_sld(
        sld_data=sld
    )

    return {
        "sld_topology": sld,
        "analysis": analysis,
        "recommendations": [
            "Verify protection coordination across topology.",
            "Verify cable sizing and voltage drop.",
            "Future graphical SLD export supported by this topology structure."
        ]
    }
