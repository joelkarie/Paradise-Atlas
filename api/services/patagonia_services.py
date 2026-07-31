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

def get_patagonia_for_apps():

    with engine.connect() as conn:

        rows = conn.execute(text("""
            select * 
            from patagonia_store_visit psv 
        """))

        return [dict(row._mapping) for row in rows]

                # SELECT psv.id, 
            # psv.store_name as name, 
            # psv.city, 
            # psv.state_province,
            # psv.address,
            # psv.postal_code,
            # psv.latitude,
            # psv.longitude 
            # FROM patagonia_store_visit psv 
            # WHERE visited = TRUE