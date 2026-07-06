import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI, Form
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from api.auth import password_hash, serializer
from api.database import engine
from api.routers.theatres_router import router as theatre_router
from api.routers.joel_could_live_router import router as joel_could_live_router
from api.routers.capitols_router import router as capitols_router
from api.routers.housing_distances_router import router as housing_distances_router
from api.routers.visit_order import router as visit_order_router
from api.routers.locations_router import router as locations_router
from api.routers.patagonia_router import router as patagonia_router
from api.routers.quaker_meetings_router import router as quaker_meetings_router
from api.routers.michael_could_live_router import router as michael_could_live_router
from api.routers.together_could_live_router import router as together_could_live_router
from api.services.locations_services import (
    get_location_ratings,
)
from api.routers.admin_router import router as admin_router

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
    admin_router,
]

for router in routers:
    app.include_router(router)


# Mount files from frontend so that they are available to the api
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


@app.get("/ping")
def ping():
    return {"ok": True}


@app.get("/admin/locations")
def admin_locations():
    return get_location_ratings()


# Serve frontend HTML pages for the main site and admin interfaces
# Each route returns the corresponding HTML file from the frontend directory.
@app.get("/")
def home():
    return FileResponse(BASE_DIR / "frontend" / "index.html")


@app.get("/login")
def login_page():
    return FileResponse(BASE_DIR / "frontend" / "login.html")


@app.post("/login")
def login(username: str = Form(), password: str = Form()):
    admin_username = os.getenv("ADMIN_USERNAME")
    admin_password_hash = os.getenv("ADMIN_PASSWORD_HASH")

    if username != admin_username:
        return {"success": False}

    if not password_hash.verify(password, admin_password_hash):
        return {"success": False}

    token = serializer.dumps({"user": username})

    response = RedirectResponse(url="/admin/home", status_code=303)

    response.set_cookie(
        key="session", value=token, httponly=True, secure=True, samesite="lax"
    )

    return response


@app.get("/logout")
def logout():
    response = RedirectResponse(url="/login")
    response.delete_cookie("session")
    return response
