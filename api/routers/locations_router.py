from fastapi import APIRouter, Form
from ..services.locations_services import get_locations, update_location_rating_value

router = APIRouter(prefix="/locations", tags=["Locations"])


@router.get("")
def locations():
    return get_locations()


@router.post("/update_location_rating")
def update_location_rating(
    location_id: str = Form(...), field: str = Form(...), value: str = Form(...)
):
    allowed_fields = {
        "joel_could_live",
        "michael_could_live",
        "joel_highlights",
        "michael_highlights",
        "joel_star_rating",
        "michael_star_rating"
    }

    if field not in allowed_fields:
        raise ValueError("Invalid field")
    
    if field in ["joel_could_live", "michael_could_live"]:
        value = True if str(value).lower() == "true" else False

    update_location_rating_value(location_id, field, value)

    return {"status": "ok"}
