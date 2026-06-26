print("🔥 API MAIN FILE LOADED")
from pathlib import Path
from api.database import engine
from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
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
from api.routers.michael_could_live_router import router as michael_could_live_router
from api.routers.together_could_live_router import router as together_could_live_router

from api.services.locations_services import get_locations, get_location_ratings

# # uvicorn app.main:app --reload

BASE_DIR = Path(__file__).resolve().parent.parent

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:5500",
        "http://localhost:5173",
        "https://paradise-atlas.onrender.com",
        "https://paradise-atlas-knx4.onrender.com",
        "https://atlas.joelkarie.com",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

routers = [
    theatre_router,
    joel_could_live_router,
    michael_could_live_router,
    capitols_router,
    housing_distances_router,
    visit_order_router,
    locations_router,
    patagonia_router,
    quaker_meetings_router,
    together_could_live_router,
]

for router in routers:
    app.include_router(router)

app.mount("/static", StaticFiles(directory="frontend"), name="static")


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


@app.post("/locations/update_could_live")
def update_location(
    location_id: str = Form(...), field: str = Form(...), could_live: str = Form(...)
):
    value = True if str(could_live).lower() == "true" else False

    with engine.begin() as conn:
        conn.exec_driver_sql(
            f"""
            UPDATE location_rating
            SET {field} = %s
            WHERE location_id = %s
        """,
            (value, location_id),
        )

    return {"status": "ok"}


@app.get("/")
def home():
    return FileResponse(BASE_DIR / "frontend" / "index.html")


@app.get("/admin/joel")
def joel_admin_page():
    return FileResponse(BASE_DIR / "frontend" / "joel_admin.html")


@app.get("/admin/michael")
def michael_admin_page():
    return FileResponse(BASE_DIR / "frontend" / "michael_admin.html")


@app.get("/ping")
def ping():
    return {"ok": True}
