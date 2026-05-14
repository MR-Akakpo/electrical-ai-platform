from sqlalchemy.orm import Session

from app.models.manufacturer_catalog_model import ManufacturerCatalogItem


def get_catalog_items(db: Session):

    return db.query(
        ManufacturerCatalogItem
    ).order_by(
        ManufacturerCatalogItem.manufacturer,
        ManufacturerCatalogItem.product_family
    ).all()


def search_catalog_items(
    db: Session,
    product_type: str | None = None,
    manufacturer: str | None = None,
    min_current_a: float | None = None
):

    query = db.query(ManufacturerCatalogItem)

    if product_type:
        query = query.filter(
            ManufacturerCatalogItem.product_type.ilike(f"%{product_type}%")
        )

    if manufacturer:
        query = query.filter(
            ManufacturerCatalogItem.manufacturer.ilike(f"%{manufacturer}%")
        )

    if min_current_a:
        query = query.filter(
            ManufacturerCatalogItem.rated_current_a >= min_current_a
        )

    return query.all()
