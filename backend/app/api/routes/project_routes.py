from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.repositories.project_repository import (
    create_project,
    get_projects,
    get_project_by_id
)


router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.post("/")
def create_new_project(
    data: dict,
    db: Session = Depends(get_db)
):

    name = data.get("name")

    if not name:
        raise HTTPException(
            status_code=400,
            detail="Project name is required"
        )

    return create_project(
        db=db,
        name=name,
        description=data.get("description")
    )


@router.get("/")
def list_projects(
    db: Session = Depends(get_db)
):

    return get_projects(db)


@router.get("/{project_id}")
def get_project(
    project_id: int,
    db: Session = Depends(get_db)
):

    project = get_project_by_id(
        db=db,
        project_id=project_id
    )

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    return project
