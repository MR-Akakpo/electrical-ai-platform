from sqlalchemy.orm import Session

from app.repositories.manufacturer_catalog_repository import (
    search_catalog_items
)


def recommend_catalog_equipment(
    db: Session,
    product_type: str,
    load_current_a: float,
    manufacturer: str | None = None
):

    items = search_catalog_items(
        db=db,
        product_type=product_type,
        manufacturer=manufacturer,
        min_current_a=load_current_a
    )

    candidates = []

    for item in items:

        candidates.append({
            "manufacturer": item.manufacturer,
            "product_family": item.product_family,
            "product_type": item.product_type,
            "reference": item.reference,
            "rated_current_a": item.rated_current_a,
            "rated_voltage_v": item.rated_voltage_v,
            "breaking_capacity_ka": item.breaking_capacity_ka,
            "poles": item.poles,
            "curve": item.curve,
            "standard": item.standard,
            "application": item.application,
            "notes": item.notes
        })

    candidates = sorted(
        candidates,
        key=lambda item: item["rated_current_a"] or 0
    )

    return {
        "requested_product_type": product_type,
        "load_current_a": load_current_a,
        "manufacturer_filter": manufacturer,
        "candidates_count": len(candidates),
        "recommended_candidates": candidates[:5],
        "note": "Catalog results depend on seeded or imported manufacturer data."
    }
