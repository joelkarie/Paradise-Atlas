from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from api.services.locations_services import get_locations

router = APIRouter(prefix="/gazetteer", tags=["Gazetteer"])

templates = Jinja2Templates(directory="frontend/templates/gazetteer")


@router.get("/home")
def gazetteer_home_page(request: Request):

    # locations = get_locations()
    locations_sorted = sorted(get_locations(), key=lambda x: x["name"].lower())

    city_count = sum(1 for location in locations_sorted if location["location_type_id"] == 1)
    parks_count = sum(1 for location in locations_sorted if location["location_type_id"] == 2)
    landmarks_count = sum(1 for location in locations_sorted if location["location_type_id"] == 3)
    
    return templates.TemplateResponse(
        request=request,
        name="gazetteer_home.html",
        context={
            "locations": locations_sorted,
            "city_count": city_count,
            "parks_count": parks_count,
            "landmarks_count": landmarks_count
        },
    )
