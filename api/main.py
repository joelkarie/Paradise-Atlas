from api.app.database import engine
from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()

from app.routers.theatres_router import router as theatre_router
from app.routers.joel_could_live_router import router as joel_could_live_router
from app.routers.capitols_router import router as capitols_router
from app.routers.housing_distances_router import router as housing_distances_router
from app.routers.visit_order import router as visit_order_router
from app.routers.locations_router import router as locations_router
from fastapi.middleware.cors import CORSMiddleware
from app.routers.patagonia_router import router as patagonia_router
from app.routers.quaker_meetings_router import router as quaker_meetings_router

# # Start Uvicorn
# # uvicorn app.main:app --reload

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Atlas Paradiso API"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
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
    result = conn.exec_driver_sql("SELECT inet_server_addr(), inet_server_port(), current_database();")
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

print("End of script")

