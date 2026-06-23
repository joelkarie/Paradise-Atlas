from sqlalchemy import text
from ..database import engine


def get_locations():

    with engine.connect() as conn:

        rows = conn.execute(text("""
            SELECT *
            FROM location l
            ORDER BY l.name
        """))

        return [dict(row._mapping) for row in rows]
