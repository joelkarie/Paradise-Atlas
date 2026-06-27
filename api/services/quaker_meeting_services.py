from sqlalchemy import text
from ..database import engine


def get_quaker_meetings():

    with engine.connect() as conn:

        rows = conn.execute(text("""
            SELECT * 
            FROM quaker_meeting_house_view
        """))

        return [dict(row._mapping) for row in rows]
