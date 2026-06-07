from fastapi import FastAPI
from sqlalchemy import create_engine, text

# Start Uvicorn
# uvicorn app.main:app --reload
app = FastAPI()


@app.get("/")
def root():
    return {"message": "Atlas Paradiso API"}


DATABASE_URL = "postgresql+psycopg://joelkarie:@localhost/atlas_paradiso"

engine = create_engine(DATABASE_URL)

# @app.get("/test-db")
# def test_db():

#     with engine.connect() as conn:

#         result = conn.execute(
#             text("SELECT COUNT(*) FROM location")
#         )

#         count = result.scalar()

#     return {
#         "locations": count
#     }


@app.get("/locations")
def locations():

    with engine.connect() as conn:

        rows = conn.execute(text("""
            SELECT *
            FROM location l
            ORDER BY l.name
        """))

        return [dict(row._mapping) for row in rows]


@app.get("/visit_order")
def visit_order():

    with engine.connect() as conn:

        rows = conn.execute(text("""
            SELECT *
            FROM visit_order_view
        """))

        return [dict(row._mapping) for row in rows]


@app.get("/housing_distances")
def housing_distances():

    with engine.connect() as conn:

        rows = conn.execute(text("""
            SELECT *
            FROM housing_distance_view hd
        """))

        return [dict(row._mapping) for row in rows]

@app.get("/capitols")
def capitols():

    with engine.connect() as conn:

        rows = conn.execute(text("""
            SELECT * 
            FROM capitol_visit_order_view
        """))
    
    return [dict(row._mapping) for row in rows]

@app.get("/joel_could_live")
def joel_could_live():

    with engine.connect() as conn:
    
        rows = conn.execute(text("""
        SELECT * 
        FROM joel_could_live_view 
        """))
    
    return [dict(row._mapping) for row in rows]


@app.get("/theatres")
def theatres():

    with engine.connect() as conn:

        rows = conn.execute(text("""
            SELECT *
            FROM theatre t
            ORDER BY t.name
        """))

        return [dict(row._mapping) for row in rows]


print("End of script")
