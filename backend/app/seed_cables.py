from app.database import SessionLocal

from app.models.cable_model import Cable


db = SessionLocal()


cables = [

    {
        "section_mm2": 1.5,
        "ampacity": 18,
        "material": "copper",
        "installation_method": "C"
    },

    {
        "section_mm2": 2.5,
        "ampacity": 24,
        "material": "copper",
        "installation_method": "C"
    },

    {
        "section_mm2": 4,
        "ampacity": 32,
        "material": "copper",
        "installation_method": "C"
    },

    {
        "section_mm2": 6,
        "ampacity": 41,
        "material": "copper",
        "installation_method": "C"
    },

    {
        "section_mm2": 10,
        "ampacity": 57,
        "material": "copper",
        "installation_method": "C"
    },

    {
        "section_mm2": 16,
        "ampacity": 76,
        "material": "copper",
        "installation_method": "C"
    },

    {
        "section_mm2": 25,
        "ampacity": 101,
        "material": "copper",
        "installation_method": "C"
    },

    {
        "section_mm2": 35,
        "ampacity": 125,
        "material": "copper",
        "installation_method": "C"
    },

    {
        "section_mm2": 50,
        "ampacity": 151,
        "material": "copper",
        "installation_method": "C"
    },

    {
        "section_mm2": 70,
        "ampacity": 192,
        "material": "copper",
        "installation_method": "C"
    },

    {
        "section_mm2": 95,
        "ampacity": 232,
        "material": "copper",
        "installation_method": "C"
    },

    {
        "section_mm2": 120,
        "ampacity": 269,
        "material": "copper",
        "installation_method": "C"
    },

    {
        "section_mm2": 150,
        "ampacity": 309,
        "material": "copper",
        "installation_method": "C"
    },

    {
        "section_mm2": 185,
        "ampacity": 353,
        "material": "copper",
        "installation_method": "C"
    },

    {
        "section_mm2": 240,
        "ampacity": 415,
        "material": "copper",
        "installation_method": "C"
    }
]


for cable in cables:

    existing = db.query(Cable).filter(
        Cable.section_mm2 == cable["section_mm2"],
        Cable.material == cable["material"],
        Cable.installation_method == cable[
            "installation_method"
        ]
    ).first()

    if not existing:

        new_cable = Cable(

            section_mm2=cable["section_mm2"],

            ampacity=cable["ampacity"],

            material=cable["material"],

            installation_method=cable[
                "installation_method"
            ]
        )

        db.add(new_cable)


db.commit()

db.close()

print(
    "IEC cable data inserted successfully!"
)