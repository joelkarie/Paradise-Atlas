from sqlalchemy import text
from ..database import engine
from fastapi import Form


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
            SELECT l.name, l.state_province, l.country, lr.joel_could_live, lr.michael_could_live, lr.location_id, lr.joel_highlights, lr.michael_highlights
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
            "michael_highlights": r[7]
        }
        for r in rows
    ]


def update_could_live_value(location_id, field, value):

    with engine.begin() as conn:
        conn.exec_driver_sql(
            f"""
            UPDATE location_rating
            SET {field} = %s
            WHERE location_id = %s
        """,
            (value, location_id),
        )
