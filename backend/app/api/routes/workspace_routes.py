from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal

from app.schemas.engineering_workspace_schema import (
    EngineeringStudyCreate,
    EngineeringStudyResponse
)

from app.repositories.engineering_workspace_repository import (
    create_engineering_study,
    get_engineering_studies
)


router = APIRouter(
    prefix="/workspace",
    tags=["Engineering Workspace"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.post(
    "/studies",
    response_model=EngineeringStudyResponse
)
def create_study(
    data: EngineeringStudyCreate,
    db: Session = Depends(get_db)
):

    return create_engineering_study(
        db=db,
        data=data.dict()
    )


@router.get(
    "/studies",
    response_model=list[EngineeringStudyResponse]
)
def list_studies(
    db: Session = Depends(get_db)
):

    return get_engineering_studies(db)
