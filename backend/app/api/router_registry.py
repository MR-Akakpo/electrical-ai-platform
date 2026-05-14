from importlib import import_module


ROUTERS = [
    ("app.api.routes.project_routes", "project_router"),
    ("app.api.routes.cable_routes", "cable_router"),
    ("app.api.routes.engineering_routes", "engineering_router"),
    ("app.api.routes.ai_routes", "ai_router"),
    ("app.api.routes.document_routes", "document_router"),
    ("app.api.routes.network_routes", "network_router"),
    ("app.api.routes.switchboard_routes", "switchboard_router"),
    ("app.api.routes.mv_switchgear_routes", "mv_switchgear_router"),
    ("app.api.routes.dc_system_routes", "dc_system_router"),
    ("app.api.routes.solar_bess_routes", "solar_bess_router"),
    ("app.api.routes.solar_pv_routes", "solar_pv_router"),
    ("app.api.routes.arc_flash_routes", "arc_flash_router"),
    ("app.api.routes.arc_flash_advanced_routes", "arc_flash_advanced_router"),
    ("app.api.routes.load_flow_routes", "load_flow_router"),
    ("app.api.routes.protection_coordination_routes", "protection_coordination_router"),
    ("app.api.routes.protection_coordination_advanced_routes", "protection_coordination_advanced_router"),
    ("app.api.routes.harmonic_routes", "harmonic_router"),
    ("app.api.routes.cable_routing_routes", "cable_routing_router"),
    ("app.api.routes.busbar_routes", "busbar_router"),
    ("app.api.routes.changeover_routes", "changeover_router"),
    ("app.api.routes.catalog_routes", "catalog_router"),
    ("app.api.routes.protection_selection_routes", "protection_selection_router"),
    ("app.api.routes.short_circuit_routes", "short_circuit_router"),
    ("app.api.routes.transformer_routes", "transformer_router"),
    ("app.api.routes.generator_routes", "generator_router"),
    ("app.api.routes.ups_routes", "ups_router"),
    ("app.api.routes.earthing_routes", "earthing_router"),
    ("app.api.routes.reactive_power_routes", "reactive_power_router"),
    ("app.api.routes.motor_routes", "motor_router"),
    ("app.api.routes.health_routes", "health_router"),
    ("app.api.routes.workspace_routes", "workspace_router"),
    ("app.api.routes.report_routes", "report_router"),
    ("app.api.routes.audit_routes", "audit_router"),
    ("app.api.routes.export_routes", "export_router"),
]


def register_all_routes(app):

    loaded_routes = []
    skipped_routes = []

    for module_path, alias in ROUTERS:

        try:
            module = import_module(module_path)
            router = getattr(module, "router")
            app.include_router(router)
            loaded_routes.append(module_path)

        except Exception as error:
            skipped_routes.append({
                "module": module_path,
                "error": str(error)
            })

    app.state.loaded_routes = loaded_routes
    app.state.skipped_routes = skipped_routes
