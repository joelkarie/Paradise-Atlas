from sqlalchemy import text
from ..database import engine


def get_theatres():

    with engine.connect() as conn:

        rows = conn.execute(text("""
            SELECT *
            FROM theatre_view t
            ORDER BY t.name
        """))

        return [dict(row._mapping) for row in rows]
