from sqlalchemy import text
from ..database import engine


def ==> ///////////////////////////////////////////////////////////
INFO:     75.188.244.172:0 - "GET /admin/joel HTTP/1.1" 200 OK
INFO:     75.188.244.172:0 - "GET /static/assets/paradise_pelican.png HTTP/1.1" 200 OK
INFO:     75.188.244.172:0 - "GET /static/css/style.css HTTP/1.1" 200 OK
INFO:     75.188.244.172:0 - "GET /admin/locations HTTP/1.1" 200 OK
INFO:     75.188.244.172:0 - "GET /admin/add_theatre HTTP/1.1" 200 OK
INFO:     75.188.244.172:0 - "GET /static/assets/no_image.webp HTTP/1.1" 404 Not Found
INFO:     75.188.244.172:0 - "GET /static/js/admin/theatre_image_upload.js HTTP/1.1" 200 OK
INFO:     75.188.244.172:0 - "POST /admin/theatres//image HTTP/1.1" 404 Not Found():

    with engine.connect() as conn:

        rows = conn.execute(text("""
            SELECT *
            FROM theatre t
            ORDER BY t.name
        """))

        return [dict(row._mapping) for row in rows]


def get_theatre(theatre_id: int):

    with engine.connect() as conn:

        row = conn.execute(
            text("""
                SELECT *
                FROM theatre_view
                WHERE id = :id
            """),
            {"id": theatre_id},
        ).first()

        if row is None:
            return None

        return dict(row._mapping)


def get_next_theatre_number():
    with engine.connect() as conn:

        result = conn.execute(text("""
            SELECT COALESCE(MAX(id), 0) + 1
            FROM theatre;
        """))

        return result.scalar_one()


def create_theatre(
    theatre_id: int,
    new_theatre_name: str,
    new_address: str,
    new_latitude: str,
    new_longitude: str,
    new_dresser: str,
):
    with engine.begin() as conn:

        result = conn.execute(
            text("""
                INSERT INTO theatre (
                    id,
                    name,
                    address,
                    latitude,
                    longitude,
                    dresser
                )
                VALUES (
                    :theatre_id,
                    :new_theatre_name,
                    :new_address,
                    :new_latitude,
                    :new_longitude,
                    :new_dresser
                )
                RETURNING id;
            """),
            {
                "theatre_id": theatre_id,
                "new_theatre_name": new_theatre_name,
                "new_address": new_address,
                "new_latitude": new_latitude,
                "new_longitude": new_longitude,
                "new_dresser": new_dresser,
            },
        )

        return result.scalar_one()
