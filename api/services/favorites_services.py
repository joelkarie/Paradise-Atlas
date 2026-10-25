from sqlalchemy import text
from ..database import engine

def get_favorite_list(column: str, topic: str):
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

