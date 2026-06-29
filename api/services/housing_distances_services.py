from sqlalchemy import text
from ..database import engine


def get_housing_distances():

    with engine.connect() as conn:

        rows = conn.execute(text("""
            SELECT * 
            FROM housing_distance_view hd       
        """))

        return [dict(row._mapping) for row in rows]
