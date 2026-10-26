from sqlalchemy import text
from ..database import engine

def get_top_ten_location_list(column: str, topic: str):
    with engine.connect() as conn:

        rows = conn.execute(
            text(f"""  
                SELECT
                    ord.position AS top_ten_order,
                    l.id,
                    l.name,
                    l.state_province,
                    l.country,
                    l.latitude,
                    l.longitude
                FROM top_tens t
                CROSS JOIN LATERAL
                    unnest(t.{column}) WITH ORDINALITY AS ord(location_id, position)
                JOIN location l ON l.id = ord.location_id
                WHERE t.name = '{topic}'
                ORDER BY ord.position;
            """))

        return [dict(row._mapping) for row in rows]

def get_top_ten_capitol_list(column: str):
    with engine.connect() as conn:

        rows = conn.execute(
            text(f"""  
                SELECT
                    ord.position AS top_ten_order,
                    c.id,
                    c.name,
                    c.country
                FROM top_tens t
                CROSS JOIN LATERAL
                    unnest(t.{column}) WITH ORDINALITY AS ord(location_id, position)
                JOIN capitol c ON c.id = ord.location_id
                WHERE t.name = 'capitol'
                ORDER BY ord.position;
            """))

        return [dict(row._mapping) for row in rows]        
