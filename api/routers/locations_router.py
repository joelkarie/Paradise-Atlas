from fastapi import APIRouter, Form
from api.services.locations_services import (
    get_locations,
    update_location_rating_value,
    get_location_types,
    get_national_parks,
)
from pydantic import BaseModel

router = APIRouter(prefix="/locations", tags=["Locations"])


@router.get("")
def locations():
    return get_locations()


@router.post("/update_location_rating")
def update_location_rating(
    location_id: str = Form(...), field: str = Form(...), value: str | None = Form(None),
):

    allowed_fields = {
        "joel_could_live",
        "michael_could_live",
        "joel_highlights",
        "michael_highlights",
        "joel_star_rating",
        "michael_star_rating",
        "restaurants"
    }

    if field not in allowed_fields:
        raise ValueError("Invalid field")

    if field in ["joel_could_live", "michael_could_live"]:
        value = True if str(value).lower() == "true" else False

    update_location_rating_value(location_id, field, value)

    return {"status": "ok"}

class LocationUpdate(BaseModel):
    location_id: int
    field: str
    value: str | None = None

@router.post("/update_location_rating_from_app")
def update_location_rating_from_app(
    update: LocationUpdate
):

    allowed_fields = {
        "joel_could_live",
        "michael_could_live",
        "joel_highlights",
        "michael_highlights",
        "joel_star_rating",
        "michael_star_rating",
        "restaurants"
    }

    if update.field not in allowed_fields:
        raise ValueError("Invalid field")

    value = update.value

    if isinstance(value, str):
        value = value.strip()
        if value == "":
            value = None

    update_location_rating_value(update.location_id, update.field, value)

    return {"status": "ok"}

@router.get("/location_types")
def location_types():
    return get_location_types()


@router.get("/national_parks")
def national_parks():
    return get_national_parks()
