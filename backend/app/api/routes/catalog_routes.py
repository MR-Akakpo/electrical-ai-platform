from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal

from app.repositories.manufacturer_catalog_repository import (
    get_catalog_items,
    search_catalog_items
)

from app.schemas.manufacturer_catalog_schema import (
    ManufacturerCatalogItemResponse
)


router = APIRouter(
    prefix="/catalog",
    tags=["Manufacturer Catalog"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.get(
    "/equipment",
    response_model=list[ManufacturerCatalogItemResponse]
)
def list_equipment_catalog(
    db: Session = Depends(get_db)
):

    return get_catalog_items(db)


@router.get(
    "/equipment/search",
    response_model=list[ManufacturerCatalogItemResponse]
)
def search_equipment_catalog(
    product_type: str | None = None,
    manufacturer: str | None = None,
    min_current_a: float | None = None,
    db: Session = Depends(get_db)
):

    return search_catalog_items(
        db=db,
        product_type=product_type,
        manufacturer=manufacturer,
        min_current_a=min_current_a
    )
