from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.db import SessionLocal
from app.schemas.project import (
    ProjectCreate,
    ProjectResponse
)

from app.repositories.project_repository import (
    create_project,
    get_projects
)

router = APIRouter()


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.post(
    "/projects",
    response_model=ProjectResponse
)
def create_new_project(
    project: ProjectCreate,
    db: Session = Depends(get_db)
):

    return create_project(db, project)


@router.get(
    "/projects",
    response_model=list[ProjectResponse]
)
def read_projects(
    db: Session = Depends(get_db)
):

    return get_projects(db)