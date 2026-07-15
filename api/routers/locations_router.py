from fastapi import APIRouter, Form
from api.services.locations_services import (
    get_locations,
    update_location_rating_value,
    get_location_types,
    get_national_parks,
)

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
        "michael_star_rating",
    }

    if field not in allowed_fields:
        raise ValueError("Invalid field")

    if field in ["joel_could_live", "michael_could_live"]:
        value = True if str(value).lower() == "true" else False

    update_location_rating_value(location_id, field, value)

    return {"status": "ok"}


@router.get("/location_types")
def location_types():
    return get_location_types()


@router.get("/national_parks")
def national_parks():
    return get_national_parks()
