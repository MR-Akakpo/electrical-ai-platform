from sqlalchemy.orm import Session

from app.models.project import Project


def create_project(

    db: Session,

    name: str,

    description: str
):

    project = Project(

        name=name,

        description=description
    )

    db.add(project)

    db.commit()

    db.refresh(project)

    return project


def get_projects(
    db: Session
):

    return db.query(
        Project
    ).all()


def get_project_by_id(

    db: Session,

    project_id: int
):

    return db.query(
        Project
    ).filter(
        Project.id == project_id
    ).first()