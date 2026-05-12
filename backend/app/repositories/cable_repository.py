from sqlalchemy.orm import Session

from app.models.cable_model import Cable


def get_cables(

    db: Session,

    material: str,

    installation_method: str
):

    return db.query(Cable).filter(

        Cable.material == material,

        Cable.installation_method
        == installation_method

    ).order_by(
        Cable.section_mm2
    ).all()