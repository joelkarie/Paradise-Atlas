from sqlalchemy import text
from ..database import engine


def get_canadian_railway_hotels(get_visited=True):

    with engine.connect() as conn:
        sql = """
            SELECT *
            FROM canadian_railway_hotels
        """

        if get_visited:
            sql += """WHERE visited = TRUE"""

        rows = conn.execute(text(sql))

        return [dict(row._mapping) for row in rows]
