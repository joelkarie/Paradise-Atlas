from sqlalchemy import text
from ..database import engine


def get_visit_order():

    with engine.connect() as conn:

        rows = conn.execute(text("""
            SELECT *
            FROM visit_order_view
        """))

        return [dict(row._mapping) for row in rows]
    
