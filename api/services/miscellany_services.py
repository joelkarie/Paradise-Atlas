from sqlalchemy import text
from ..database import engine


def get_top_ten_location_list(column: str, topic: str):
    with engine.connect() as conn:

        rows = conn.execute(text(f"""  
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

        rows = conn.execute(text(f"""  
                SELECT
                    ord.position AS top_ten_order,
                    c.id,
                    c.name,
                    l.name as state_province,
                    c.country
                FROM top_tens t
                CROSS JOIN LATERAL
                    unnest(t.{column}) WITH ORDINALITY AS ord(location_id, position)
                JOIN capitol c
                    ON c.id = ord.location_id
                LEFT JOIN LATERAL (
                    SELECT v.location_id
                    FROM visit v
                    WHERE v.capitol_id = c.id
                    ORDER BY v.date DESC
                    LIMIT 1
                ) v ON TRUE
                LEFT JOIN location l
                    ON l.id = v.location_id
                WHERE t.name = 'capitol'
                ORDER BY ord.position;
            """))

        return [dict(row._mapping) for row in rows]


def get_top_ten_canadian_railway_hotel_list(column: str):
    with engine.connect() as conn:

        rows = conn.execute(text(f"""  
                SELECT
                    ord.position AS top_ten_order,
                    crh.id,
                    crh.name,
                    crh.province AS state_province,
                    'Canada' AS country,
                    crh.latitude,
                    crh.longitude
                FROM top_tens t
                CROSS JOIN LATERAL
                    unnest(t.{column}) WITH ORDINALITY AS ord(location_id, position)
                JOIN canadian_railway_hotels crh ON crh.id = ord.location_id
                WHERE t.name = 'canadian railway hotel'
                ORDER BY ord.position;
            """))

        return [dict(row._mapping) for row in rows]


def get_top_ten_theatres_list(column: str):
    with engine.connect() as conn:

        rows = conn.execute(text(f"""  
                SELECT
                    ord.position AS top_ten_order,
                    th.id,
                    th.name,
                    l.state_province,
                    l.country
                FROM top_tens t
                CROSS JOIN LATERAL
                    unnest(t.{column}) WITH ORDINALITY AS ord(location_id, position)
                JOIN theatre th
                    ON th.id = ord.location_id
                LEFT JOIN LATERAL (
                    SELECT v.location_id
                    FROM visit v
                    WHERE v.theatre_id = th.id
                    ORDER BY v.date DESC
                    LIMIT 1
                ) v ON TRUE
                LEFT JOIN location l
                    ON l.id = v.location_id
                WHERE t.name = 'theatre'
                ORDER BY ord.position;
            """))

        return [dict(row._mapping) for row in rows]

def get_top_ten_quaker_meeting_list(column: str):
    with engine.connect() as conn:

        rows = conn.execute(text(f"""  
                SELECT
                    ord.position AS top_ten_order,
                    q.id,
                    q.name,
                    q.state_province,
                    q.country,
                    q.latitude,
                    q.longitude
                FROM top_tens t
                CROSS JOIN LATERAL
                    unnest(t.{column}) WITH ORDINALITY AS ord(location_id, position)
                JOIN quaker_meeting_house q ON q.id = ord.location_id
                WHERE t.name = 'quaker'
                ORDER BY ord.position;
            """))

        return [dict(row._mapping) for row in rows]

def get_top_ten_patagonia_list(column: str):
    with engine.connect() as conn:

        rows = conn.execute(text(f"""  
                SELECT
                    ord.position AS top_ten_order,
                    p.id,
                    p.store_name AS name,
                    p.state_province,
                    p.country,
                    p.latitude,
                    p.longitude
                FROM top_tens t
                CROSS JOIN LATERAL
                    unnest(t.{column}) WITH ORDINALITY AS ord(location_id, position)
                JOIN patagonia_store_visit p ON p.id = ord.location_id
                WHERE t.name = 'quaker'
                ORDER BY ord.position;
            """))

        return [dict(row._mapping) for row in rows]