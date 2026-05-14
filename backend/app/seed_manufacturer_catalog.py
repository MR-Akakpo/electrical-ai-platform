from app.database import SessionLocal

from app.models.manufacturer_catalog_model import ManufacturerCatalogItem


db = SessionLocal()


items = [
    {
        "manufacturer": "Schneider Electric",
        "product_family": "Compact NSX",
        "product_type": "MCCB",
        "reference": "NSX250",
        "rated_current_a": 250,
        "rated_voltage_v": 690,
        "breaking_capacity_ka": 36,
        "poles": 3,
        "curve": "Electronic/Thermal magnetic",
        "standard": "IEC 60947-2",
        "application": "LV distribution protection",
        "technical_data": {
            "adjustable_trip": True,
            "category": "MCCB"
        },
        "source_document": "manufacturer_catalog_pending",
        "notes": "Initial placeholder catalog item. Replace with verified manufacturer data."
    },
    {
        "manufacturer": "ABB",
        "product_family": "Tmax",
        "product_type": "MCCB",
        "reference": "Tmax XT",
        "rated_current_a": 160,
        "rated_voltage_v": 690,
        "breaking_capacity_ka": 36,
        "poles": 3,
        "curve": "Thermal magnetic / electronic",
        "standard": "IEC 60947-2",
        "application": "LV feeder protection",
        "technical_data": {
            "category": "MCCB"
        },
        "source_document": "manufacturer_catalog_pending",
        "notes": "Initial placeholder catalog item. Replace with verified manufacturer data."
    }
]


for item in items:

    exists = db.query(
        ManufacturerCatalogItem
    ).filter(
        ManufacturerCatalogItem.manufacturer == item["manufacturer"],
        ManufacturerCatalogItem.reference == item["reference"]
    ).first()

    if not exists:

        db.add(
            ManufacturerCatalogItem(**item)
        )


db.commit()
db.close()

print("Manufacturer catalog seeded successfully!")
