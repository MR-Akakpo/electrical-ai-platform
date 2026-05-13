from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.project_routes import router as project_router
from app.api.routes.cable_routes import router as cable_router
from app.api.routes.engineering_routes import router as engineering_router
from app.api.routes.ai_routes import router as ai_router


app = FastAPI(
    title="Electrical AI Platform API",
    description="High-level backend for electrical engineering sizing, protection, standards, documents and AI/RAG integration.",
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


@app.get("/")
def root():

    return {
        "message": "Electrical AI Platform API Running",
        "status": "online"
    }
