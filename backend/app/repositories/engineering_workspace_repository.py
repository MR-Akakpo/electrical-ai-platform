from sqlalchemy.orm import Session

from app.models.engineering_study_model import (
    EngineeringStudy
)


def create_engineering_study(
    db: Session,
    data: dict
):

    study = EngineeringStudy(**data)

    db.add(study)

    db.commit()

    db.refresh(study)

    return study


def get_engineering_studies(
    db: Session
):

    return db.query(
        EngineeringStudy
    ).all()
