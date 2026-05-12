from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes.project_routes import router as project_router
from app.api.routes.cable_routes import router as cable_router

app = FastAPI()
app.include_router(cable_router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(project_router)


@app.get("/")
def root():

    return {
        "message": "Electrical AI Platform API Running"
    }