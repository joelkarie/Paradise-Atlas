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
