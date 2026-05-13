from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.project_routes import router as project_router
from app.api.routes.cable_routes import router as cable_router
from app.api.routes.engineering_routes import router as engineering_router
from app.api.routes.ai_routes import router as ai_router
from app.api.routes.document_routes import router as document_router
from app.api.routes.network_routes import router as network_router
from app.api.routes.switchboard_routes import router as switchboard_router
from app.api.routes.mv_switchgear_routes import router as mv_switchgear_router
from app.api.routes.dc_system_routes import router as dc_system_router
from app.api.routes.solar_bess_routes import router as solar_bess_router
from app.api.routes.arc_flash_routes import router as arc_flash_router
from app.api.routes.load_flow_routes import router as load_flow_router
from app.api.routes.protection_coordination_routes import router as protection_coordination_router
from app.api.routes.harmonic_routes import router as harmonic_router
from app.api.routes.cable_routing_routes import router as cable_routing_router
from app.api.routes.busbar_routes import router as busbar_router


app = FastAPI(
    title="Electrical AI Platform API",
    description="High-level backend for electrical engineering sizing, protection, standards, documents, networks and AI/RAG integration.",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:3001"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(project_router)
app.include_router(cable_router)
app.include_router(engineering_router)
app.include_router(ai_router)
app.include_router(document_router)
app.include_router(network_router)
app.include_router(switchboard_router)
app.include_router(mv_switchgear_router)
app.include_router(dc_system_router)
app.include_router(solar_bess_router)
app.include_router(arc_flash_router)
app.include_router(load_flow_router)
app.include_router(protection_coordination_router)
app.include_router(harmonic_router)
app.include_router(cable_routing_router)
app.include_router(busbar_router)


@app.get("/")
def root():

    return {
        "message": "Electrical AI Platform API Running",
        "status": "online"
    }
