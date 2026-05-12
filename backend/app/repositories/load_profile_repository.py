from sqlalchemy.orm import Session

from app.models.load_profile_model import LoadProfile


def get_load_profiles(db: Session):

    return db.query(
        LoadProfile
    ).order_by(
        LoadProfile.name
    ).all()


def get_load_profile_by_name(
    db: Session,
    name: str
):

    return db.query(
        LoadProfile
    ).filter(
        LoadProfile.name == name
    ).first()