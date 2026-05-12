from app.database import SessionLocal

from app.models.ampacity_table_model import (
    AmpacityTable
)


db = SessionLocal()


IEC_DATA = [

    {
        "standard": "IEC",

        "material": "copper",

        "insulation": "xlpe",

        "installation_method": "C",

        "section_mm2": 1.5,

        "ampacity": 19
    },

    {
        "standard": "IEC",

        "material": "copper",

        "insulation": "xlpe",

        "installation_method": "C",

        "section_mm2": 2.5,

        "ampacity": 26
    },

    {
        "standard": "IEC",

        "material": "copper",

        "insulation": "xlpe",

        "installation_method": "C",

        "section_mm2": 4,

        "ampacity": 34
    },

    {
        "standard": "IEC",

        "material": "copper",

        "insulation": "xlpe",

        "installation_method": "C",

        "section_mm2": 6,

        "ampacity": 44
    },

    {
        "standard": "IEC",

        "material": "copper",

        "insulation": "xlpe",

        "installation_method": "C",

        "section_mm2": 10,

        "ampacity": 61
    },

    {
        "standard": "IEC",

        "material": "copper",

        "insulation": "xlpe",

        "installation_method": "C",

        "section_mm2": 16,

        "ampacity": 82
    },

    {
        "standard": "IEC",

        "material": "copper",

        "insulation": "xlpe",

        "installation_method": "C",

        "section_mm2": 25,

        "ampacity": 108
    },

    {
        "standard": "IEC",

        "material": "copper",

        "insulation": "xlpe",

        "installation_method": "C",

        "section_mm2": 35,

        "ampacity": 134
    },

    {
        "standard": "IEC",

        "material": "copper",

        "insulation": "xlpe",

        "installation_method": "C",

        "section_mm2": 50,

        "ampacity": 162
    },

    {
        "standard": "IEC",

        "material": "copper",

        "insulation": "xlpe",

        "installation_method": "C",

        "section_mm2": 70,

        "ampacity": 208
    },

    {
        "standard": "IEC",

        "material": "copper",

        "insulation": "xlpe",

        "installation_method": "C",

        "section_mm2": 95,

        "ampacity": 250
    },

    {
        "standard": "IEC",

        "material": "copper",

        "insulation": "xlpe",

        "installation_method": "C",

        "section_mm2": 120,

        "ampacity": 290
    },

    {
        "standard": "IEC",

        "material": "copper",

        "insulation": "xlpe",

        "installation_method": "C",

        "section_mm2": 150,

        "ampacity": 334
    },

    {
        "standard": "IEC",

        "material": "copper",

        "insulation": "xlpe",

        "installation_method": "C",

        "section_mm2": 185,

        "ampacity": 382
    },

    {
        "standard": "IEC",

        "material": "copper",

        "insulation": "xlpe",

        "installation_method": "C",

        "section_mm2": 240,

        "ampacity": 467
    }
]


for data in IEC_DATA:

    existing = (

        db.query(AmpacityTable)

        .filter(
            AmpacityTable.material
            == data["material"]
        )

        .filter(
            AmpacityTable.insulation
            == data["insulation"]
        )

        .filter(
            AmpacityTable.installation_method
            == data["installation_method"]
        )

        .filter(
            AmpacityTable.section_mm2
            == data["section_mm2"]
        )

        .first()
    )


    if not existing:

        record = AmpacityTable(

            standard=data["standard"],

            material=data["material"],

            insulation=data["insulation"],

            installation_method=data[
                "installation_method"
            ],

            section_mm2=data["section_mm2"],

            ampacity=data["ampacity"]
        )

        db.add(record)


db.commit()

db.close()

print(
    "IEC ampacity tables seeded successfully!"
)