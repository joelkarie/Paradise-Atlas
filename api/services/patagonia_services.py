from sqlalchemy import text
from ..database import engine


def get_patagonia_stores():

    with engine.connect() as conn:

        rows = conn.execute(text("""
            SELECT *
            FROM patagonia_visit_view
            WHERE visited = TRUE
        """))

        return [dict(row._mapping) for row in rows]