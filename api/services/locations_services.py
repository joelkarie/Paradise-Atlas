from sqlalchemy import text
from ..database import engine


def get_locations():

    with engine.connect() as conn:

        rows = conn.execute(text("""
            SELECT *
            FROM location l
            JOIN location_rating lr
            ON l.id = lr.location_id;
        """))

        return [dict(row._mapping) for row in rows]


def get_location_ratings():
    with engine.connect() as conn:
        result = conn.exec_driver_sql("""
            SELECT l.name, l.state_province, l.country, 
            lr.joel_could_live, lr.michael_could_live, lr.location_id, 
            lr.joel_highlights, lr.michael_highlights, lr.joel_star_rating, lr.michael_star_rating
            FROM location l 
            JOIN location_rating lr ON lr.location_id = l.id
            WHERE l.location_type_id = 1
            ORDER BY l.name ASC
        """)
        rows = result.fetchall()

    return [
        {
            "location": r[0],
            "state": r[1],
            "country": r[2],
            "joel_could_live": r[3],
            "michael_could_live": r[4],
            "location_id": r[5],
            "joel_highlights": r[6],
            "michael_highlights": r[7],
            "joel_star_rating": r[8],
            "michael_star_rating": r[9],
        }
        for r in rows
    ]


def update_location_rating_value(location_id, field, value):

    with engine.begin() as conn:
        conn.exec_driver_sql(
            f"""
            UPDATE location_rating
            SET {field} = %s
            WHERE location_id = %s
        """,
            (value, location_id),
        )

def get_location_types():

    with engine.connect() as conn:

        rows = conn.execute(text("""
            SELECT
                id,
                name
            FROM location_type
            ORDER BY name;
        """))

        return [dict(row._mapping) for row in rows]
    
def get_locations_for_dropdown():
    with engine.connect() as conn:

        rows = conn.execute(text("""
            SELECT
                id,
                name,
                state_province,
                country
            FROM location
            ORDER BY LOWER(name) ASC;
        """))

        return [dict(row._mapping) for row in rows]
    
def create_location(
        name, 
        location_type_id,
        state_province,
        country,
):
    with engine.begin() as conn:

        result = conn.execute(
            text("""
                INSERT INTO location (
                    name,
                    census_name,
                    location_type_id,
                    state_province,
                    country
                )
                VALUES (
                    :name,
                    :census_name,
                    :location_type_id,
                    :state_province,
                    :country
                )
                RETURNING id;
            """),
            {
                "name": name,
                "census_name": name,
                "location_type_id": location_type_id,
                "state_province": state_province,
                "country": country,
            },
        )

        return result.scalar_one()


def create_location_rating(location_id: int):
    with engine.begin() as conn:
        conn.execute(
            text("""
                INSERT INTO location_rating (
                    location_id
                )
                VALUES (:location_id)
            """),
            {"location_id": location_id},
        )

def get_national_parks():
    with engine.connect() as conn:

        rows = conn.execute(text("""
            select 
                *
            from location l
            where l.location_type_id = 2;
        """))

        return [dict(row._mapping) for row in rows]
