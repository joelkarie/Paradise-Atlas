from sqlalchemy import text
from ..database import engine

def get_top_ten_location_list(column: str, topic: str):
    with engine.connect() as conn:

        rows = conn.execute(
            text(f"""  
                SELECT
                    fav.position AS favorite_order,
                    l.id,
                    l.name AS city,
                    l.state_province,
                    l.country,
                    l.latitude,
                    l.longitude
                FROM favorites f
                CROSS JOIN LATERAL
                    unnest(f.{column}) WITH ORDINALITY AS fav(location_id, position)
                JOIN location l ON l.id = fav.location_id
                WHERE f.name = '{topic}'
                ORDER BY fav.position;
            """))

        return [dict(row._mapping) for row in rows]

def get_top_ten_capitol_list(column: str):
    with engine.connect() as conn:

        rows = conn.execute(
            text(f"""  
                SELECT
                    fav.position AS favorite_order,
                    c.id,
                    c.name,
                    c.country
                FROM favorites f
                CROSS JOIN LATERAL
                    unnest(f.{column}) WITH ORDINALITY AS fav(location_id, position)
                JOIN capitol c ON c.id = fav.location_id
                WHERE f.name = 'capitol'
                ORDER BY fav.position;
            """))

        return [dict(row._mapping) for row in rows]        

#         rows = conn.execute(text("""
#             SELECT * 
#             FROM capitol_visit_order_view
#         """))