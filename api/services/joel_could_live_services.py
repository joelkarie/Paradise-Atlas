from sqlalchemy import text
from ..database import engine


def get_joel_could_live():

    with engine.connect() as conn:

        rows = conn.execute(text("""
            SELECT * 
            FROM joel_could_live_view 
        """))

        return [dict(row._mapping) for row in rows]
