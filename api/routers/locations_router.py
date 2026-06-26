from fastapi import APIRouter, Form
from ..services.locations_services import get_locations, update_could_live_value

router = APIRouter(prefix="/locations", tags=["Locations"])


@router.get("")
def locations():
    return get_locations()

@router.post("/locations/update_could_live")
def update_could_live(
    location_id: str = Form(...),
    field: str = Form(...),
    could_live: str = Form(...)
):
    value = True if str(could_live).lower() == "true" else False

    update_could_live_value(
        location_id,
        field,
        value
    )

    return {"status": "ok"}