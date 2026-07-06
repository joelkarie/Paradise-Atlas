from sqlalchemy import text
from ..database import engine


def get_housing_distances():

    with engine.connect() as conn:

        rows = conn.execute(text("""
            SELECT * 
            FROM housing_distance_view hd       
        """))

        return [dict(row._mapping) for row in rows]


def get_digs_types():

    with engine.connect() as conn:

        rows = conn.execute(text("""
            SELECT
                id,
                name
            FROM digs_type
            ORDER BY id;
        """))

        return [dict(row._mapping) for row in rows]

def get_next_digs_number():
    with engine.connect() as conn:

        result = conn.execute(text("""
            SELECT COALESCE(MAX(visit_number), 0) + 1
            FROM digs;
        """))

        return result.scalar_one()

# def create_digs(
#     digs_id: int,
#     digs_type_id: int,
#     new_address: str,
#     new_latitude: str,
#     new_longitude: str,
#     company_housing_bool: bool,
# ):
#     with engine.begin() as conn:

#         result = conn.execute(
#             text("""
#                 INSERT INTO visit (
#                     location_id,
#                     date,
#                     visit_number,
#                     visit_order
#                 )
#                 VALUES (
#                     :location_id,
#                     :visit_date,
#                     :visit_number,
#                     :visit_order
#                 )
#                 RETURNING id;
#             """),
#             {
#                 "location_id": location_id,
#                 "visit_date": visit_date,
#                 "visit_number": visit_number,
#                 "visit_order": visit_order,
#             },
#         )

#         return result.scalar_one()