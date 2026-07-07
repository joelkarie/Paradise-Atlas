from sqlalchemy import text
from ..database import engine


def get_housing_distances():

    with engine.connect() as conn:

        rows = conn.execute(text("""
            SELECT * 
            FROM housing_distance_view hd       
        """))

        return [dict(row._mapping) for row in rows]


def get_digs_types():

    with engine.connect() as conn:

        rows = conn.execute(text("""
            SELECT
                id,
                name
            FROM digs_type
            ORDER BY id;
        """))

        return [dict(row._mapping) for row in rows]

def get_next_digs_number():
    with engine.connect() as conn:

        result = conn.execute(text("""
            SELECT COALESCE(MAX(id), 0) + 1
            FROM digs;
        """))

        return result.scalar_one()

def create_digs(
    digs_id: int,
    digs_type_id: int,
    new_address: str,
    new_latitude: str,
    new_longitude: str,
    company_housing_bool: bool,
):
    with engine.begin() as conn:

        result = conn.execute(
            text("""
                INSERT INTO digs (
                    id,
                    address,
                    latitude,
                    longitude,
                    digs_type_id,
                    company_housing,
                )
                VALUES (
                    :digs_id,
                    :new_address,
                    :new_latitude,
                    :new_longitude,
                    :digs_type_id,
                    :company_housing_bool,
                )
                RETURNING id;
            """),
            {
                "digs_id": digs_id,
                "new_address": new_address,
                "new_latitude": new_latitude,
                "new_longitude": new_longitude,
                "digs_type_id": digs_type_id,
                "company_housing_bool": company_housing_bool,
            },
        )

        return result.scalar_one()