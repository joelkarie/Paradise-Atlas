from sqlalchemy import text
from ..database import engine


def get_capitols():

    with engine.connect() as conn:

        rows = conn.execute(text("""
            SELECT * 
            FROM capitol_visit_order_view
        """))

        return [dict(row._mapping) for row in rows]

def get_capitols_for_app():

    with engine.connect() as conn:

        rows = conn.execute(text("""
            SELECT
                cap.id AS id, 
                l.name AS city, 
                l.state_province AS state_province, 

                ARRAY_AGG(v."date" ORDER BY v."date") AS dates,

                cap.latitude AS latitude, 
                cap.longitude AS longitude, 
                cap.fact AS fact, 
                cap.architect AS architect, 
                cap.architectural_style AS architectural_style, 
                cap.year_completed AS year_completed

            FROM visit v
            JOIN location l ON l.id = v.location_id
            JOIN capitol cap ON cap.id = v.capitol_id

            GROUP BY
                cap.id,
                l.name,
                l.state_province,
                l.latitude,
                l.longitude,
                cap.fact,
                cap.architect,
                cap.architectural_style,
                cap.year_completed

            ORDER BY l.state_province ASC
        """))

        return [dict(row._mapping) for row in rows]