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
                    date,
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


def get_visits_for_dropdown(without_digs=False):
    with engine.connect() as conn:

        sql = """
            SELECT
                v.id AS id,
                v.visit_number AS visit_number,
                l.name AS location_name,
                l.state_province AS state_province,
                v.date AS date
            FROM visit v
            JOIN location l
                ON l.id = v.location_id
        """

        if without_digs:
            sql += " WHERE v.digs_id IS NULL"

        sql += " ORDER BY v.visit_number ASC"

        rows = conn.execute(text(sql))

        return [dict(row._mapping) for row in rows]


def add_digs_to_visit(visit_id: int, digs_id: int) -> bool:
    with engine.begin() as conn:

        result = conn.execute(
            text("""
                UPDATE visit
                SET digs_id = :digs_id,
                    updated_at = NOW()
                WHERE id = :visit_id;
            """),
            {
                "visit_id": visit_id,
                "digs_id": digs_id,
            },
        )

        return result.rowcount == 1


def add_theatre_to_visit(visit_id: int, theatre_id: int) -> bool:
    with engine.begin() as conn:

        result = conn.execute(
            text("""
                UPDATE visit
                SET theatre_id = :theatre_id,
                    updated_at = NOW()
                WHERE id = :visit_id;
            """),
            {
                "visit_id": visit_id,
                "theatre_id": theatre_id,
            },
        )

        return result.rowcount == 1
