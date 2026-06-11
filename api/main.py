from fastapi import FastAPI

from app.routers.theatres_router import router as theatre_router
from app.routers.joel_could_live_router import router as joel_could_live_router
from app.routers.capitols_router import router as capitols_router
from app.routers.housing_distances_router import router as housing_distances_router
from app.routers.visit_order import router as visit_order_router
from app.routers.locations_router import router as locations_router

app = FastAPI()

app.include_router(theatre_router)
app.include_router(joel_could_live_router)
app.include_router(capitols_router)
app.include_router(housing_distances_router)
app.include_router(visit_order_router)
app.include_router(locations_router)

print("End of script")
