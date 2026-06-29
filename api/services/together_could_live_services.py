from sqlalchemy import text
from ..database import engine


def get_together_could_live():

    with engine.connect() as conn:

        rows = conn.execute(text("""
            SELECT 
                l.name AS city, l.state_province AS state_province, l.country AS country, 
                l.latitude AS latitude, l.longitude AS longitude
            FROM location l 
            JOIN location_rating lr ON lr.location_id = l.id
            WHERE lr.michael_could_live = True AND lr.joel_could_live = True 
            ORDER BY l.name ASC
        """))

        return [dict(row._mapping) for row in rows]
