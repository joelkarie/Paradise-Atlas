from sqlalchemy import text
from ..database import engine


def get_theatres():

    with engine.connect() as conn:

        rows = conn.execute(text("""
            SELECT t.name AS name, 
            l.name AS city, 
            l.state_province AS state_province, 
            v.date AS date, l.latitude AS latitude, 
            l.longitude AS longitude,
            t.id as id
            FROM visit v
            JOIN theatre t ON t.id = v.theatre_id
            JOIN location l ON l.id = v.location_id
            ORDER by name ASC
        """))

        return [dict(row._mapping) for row in rows]

def get_all_theatres_data():

    with engine.connect() as conn:

        rows = conn.execute(text("""
            SELECT *
            FROM theatre t
            ORDER BY t.name
        """))

        return [dict(row._mapping) for row in rows]


def get_theatre(theatre_id: int):

    with engine.connect() as conn:

        row = conn.execute(
            text("""
                SELECT *
                FROM theatre
                WHERE id = :id
            """),
            {"id": theatre_id},
        ).first()

        if row is None:
            return None

        return dict(row._mapping)


def get_next_theatre_number():
    with engine.connect() as conn:

        result = conn.execute(text("""
            SELECT COALESCE(MAX(id), 0) + 1
            FROM theatre;
        """))

        return result.scalar_one()


def create_theatre(
    theatre_id: int,
    new_theatre_name: str,
    new_address: str,
    new_latitude: str,
    new_longitude: str,
    new_dresser: str,
):
    with engine.begin() as conn:

        result = conn.execute(
            text("""
                INSERT INTO theatre (
                    id,
                    name,
                    address,
                    latitude,
                    longitude,
                    dresser
                )
                VALUES (
                    :theatre_id,
                    :new_theatre_name,
                    :new_address,
                    :new_latitude,
                    :new_longitude,
                    :new_dresser
                )
                RETURNING id;
            """),
            {
                "theatre_id": theatre_id,
                "new_theatre_name": new_theatre_name,
                "new_address": new_address,
                "new_latitude": new_latitude,
                "new_longitude": new_longitude,
                "new_dresser": new_dresser,
            },
        )

        return result.scalar_one()
