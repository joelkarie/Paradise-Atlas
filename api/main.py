from api.database import engine
from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
from dotenv import load_dotenv
import os

load_dotenv()

from api.routers.theatres_router import router as theatre_router
from api.routers.joel_could_live_router import router as joel_could_live_router
from api.routers.capitols_router import router as capitols_router
from api.routers.housing_distances_router import router as housing_distances_router
from api.routers.visit_order import router as visit_order_router
from api.routers.locations_router import router as locations_router
from fastapi.middleware.cors import CORSMiddleware
from api.routers.patagonia_router import router as patagonia_router
from api.routers.quaker_meetings_router import router as quaker_meetings_router

from api.services.locations_services import get_locations, get_location_ratings

# # uvicorn app.main:app --reload

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Atlas Paradiso API"}


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:5500",
        "http://localhost:5173",
        "https://paradise-atlas.onrender.com",
        "https://paradise-atlas-knx4.onrender.com",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(theatre_router)
app.include_router(joel_could_live_router)
app.include_router(capitols_router)
app.include_router(housing_distances_router)
app.include_router(visit_order_router)
app.include_router(locations_router)
app.include_router(patagonia_router)
app.include_router(quaker_meetings_router)


@app.get("/db-info")
def db_info():
    conn = engine.connect()
    result = conn.exec_driver_sql(
        "SELECT inet_server_addr(), inet_server_port(), current_database();"
    )
    row = result.fetchone()
    conn.close()

    return {
        "ip": row[0],
        "port": row[1],
        "database": row[2],
    }


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/admin/locations")
def admin_locations():
    return get_location_ratings()


@app.post("/locations/update")
def update_location(location_id: str = Form(...), joel_could_live: str = Form(...)):
    value = True if str(joel_could_live).lower() == "true" else False

    with engine.begin() as conn:
        conn.exec_driver_sql(
            """
            UPDATE location_rating
            SET joel_could_live = %s
            WHERE location_id = %s
        """,
            (value, location_id),
        )

    return {"status": "ok"}

@app.get("/admin")
def admin_page():
    return FileResponse("frontend/joel_admin.html")