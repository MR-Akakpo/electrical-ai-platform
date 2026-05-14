from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.router_registry import register_all_routes


app = FastAPI(
    title="Electrical AI Platform API",
    description="High-level backend for electrical engineering sizing, protection, catalogs, studies and AI/RAG integration.",
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

register_all_routes(app)


@app.get("/")
def root():

    return {
        "message": "Electrical AI Platform API Running",
        "status": "online",
        "loaded_routes": app.state.loaded_routes,
        "skipped_routes": app.state.skipped_routes
    }



