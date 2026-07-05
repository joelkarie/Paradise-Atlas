from sqlalchemy import text
from ..database import engine


def get_visit_order():

    with engine.connect() as conn:

        rows = conn.execute(text("""
            SELECT *
            FROM visit_order_view
        """))

        return [dict(row._mapping) for row in rows]

def get_next_visit_number():
    with engine.connect() as conn:

        result = conn.execute(text("""
            SELECT COALESCE(MAX(visit_number), 0) + 1
            FROM visit;
        """))

        return result.scalar_one()

def get_next_visit_order():
    with engine.connect() as conn:

        result = conn.execute(text("""
            SELECT COALESCE(MAX(visit_order), 0) + 1
            FROM visit;
        """))

        return result.scalar_one()


def create_visit(
    location_id: int,
    visit_date: str,
    visit_number: int,
    visit_order: int,
):
    with engine.begin() as conn:

        result = conn.execute(
            text("""
                INSERT INTO visit (
                    location_id,
                    visit_date,
                    visit_number,
                    visit_order
                )
                VALUES (
                    :location_id,
                    :visit_date,
                    :visit_number,
                    :visit_order
                )
                RETURNING id;
            """),
            {
                "location_id": location_id,
                "visit_date": visit_date,
                "visit_number": visit_number,
                "visit_order": visit_order,
            },
        )

        return result.scalar_one()