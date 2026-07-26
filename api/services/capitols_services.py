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
            cap.id as id, 
            l.name as city, 
            l.state_province as state_province, 
            v."date" as date,
            l.latitude AS latitude, 
            l.longitude AS longitude, 
            cap.fact AS fact, cap.architect AS architect, 
            cap.architectural_style AS architectural_style, 
            cap.year_completed AS year_completed
            FROM visit v
            JOIN location l on l.id = v.location_id
            JOIN capitol cap ON cap.id = v.capitol_id
            ORDER BY l.state_province ASC
        """))

        return [dict(row._mapping) for row in rows]