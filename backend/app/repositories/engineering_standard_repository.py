from sqlalchemy.orm import Session

from app.models.engineering_standard_model import EngineeringStandard


def get_standards(db: Session):

    return db.query(
        EngineeringStandard
    ).order_by(
        EngineeringStandard.code
    ).all()


def get_standard_by_code(
    db: Session,
    code: str
):

    return db.query(
        EngineeringStandard
    ).filter(
        EngineeringStandard.code == code
    ).first()