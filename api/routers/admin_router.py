from fastapi import APIRouter, Request, Form
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from pathlib import Path
from pydantic import BaseModel


from api.auth import require_admin
from api.services.locations_services import (
    get_location_ratings,
    get_location_types,
    get_locations_for_dropdown,
    create_location,
    create_location_rating,
    create_building_details,
    get_cities_for_dropdown,
    get_cityhalls,
    get_libraries,
    get_national_parks,
    get_buildings,
    get_museums,
)
from api.services.visit_services import (
    get_next_visit_number,
    get_next_visit_order,
    create_visit,
    get_visits_for_dropdown,
    add_digs_to_visit,
    add_theatre_to_visit,
)
from api.services.digs_services import get_digs_types, get_next_digs_number, create_digs

from api.services.theatre_services import (
    get_next_theatre_number,
    create_theatre,
    get_all_theatres_data,
    get_theatres_for_app,
)

from api.services.miscellany_services import (
    get_top_ten_location_list,
    get_top_ten_capitol_list,
    get_top_ten_canadian_railway_hotel_list,
    get_top_ten_theatres_list,
    get_top_ten_quaker_meeting_list,
)

from api.services.capitols_services import get_capitols

from api.services.canadian_railway_hotel_services import (
    get_canadian_railway_hotels_for_dropdown,
)

from api.services.quaker_meeting_services import get_quaker_meetings_for_dropdown

BASE_DIR = Path(__file__).resolve().parent.parent.parent

router = APIRouter(prefix="/admin")

templates = Jinja2Templates(directory="frontend/templates")


def article_for(word):
    return "an" if word and word[0].lower() in "aeiou" else "a"


templates.env.filters["article"] = article_for


@router.get("/locations")
def admin_locations():
    return get_location_ratings()


@router.get("/home")
def admin_home_page(request: Request):
    try:
        user = require_admin(request)
    except Exception:
        return RedirectResponse("/login")

    return templates.TemplateResponse(
        request=request,
        name="admin_home.html",
        context={"success": request.query_params.get("success")},
    )


@router.get("/joel")
def joel_admin_page(request: Request):
    try:
        user = require_admin(request)
    except Exception:
        return RedirectResponse("/login")

    return templates.TemplateResponse(
        request=request,
        name="/admin/admin_joel.html",
    )


@router.get("/michael")
def michael_admin_page(request: Request):
    try:
        user = require_admin(request)
    except Exception:
        return RedirectResponse("/login")

    return templates.TemplateResponse(
        request=request,
        name="/admin/admin_michael.html",
    )


@router.get("/generic_joel")
def joel_generic_admin_page(request: Request):
    try:
        user = require_admin(request)
    except Exception:
        return RedirectResponse("/login")

    return templates.TemplateResponse(
        request=request,
        name="/admin/admin_template.html",
        context={
            "user_name": "Joel",
            "background_color": "var(--primary-highlight-color)",
        },
    )


@router.get("/generic_michael")
def michael_generic_admin_page(request: Request):
    try:
        user = require_admin(request)
    except Exception:
        return RedirectResponse("/login")

    return templates.TemplateResponse(
        request=request,
        name="/admin/admin_template.html",
        context={
            "user_name": "Michael",
            "background_color": "var(--primary-highlight-color)",
        },
    )


@router.get("/add_visit")
def add_visit_page(request: Request):
    try:
        user = require_admin(request)
    except Exception:
        return RedirectResponse("/login")

    location_types = get_location_types()
    locations = get_locations_for_dropdown()

    return templates.TemplateResponse(
        request=request,
        name="add_visit.html",
        context={
            "location_types": location_types,
            "locations": locations,
        },
    )


@router.get("/update_top_ten")
def add_update_top_ten_page(request: Request):
    try:
        user = require_admin(request)
    except Exception:
        return RedirectResponse("/login")

    top_ten_lists = [
        (
            "Cities",
            "city",
            get_top_ten_location_list("joel", "city"),
            get_top_ten_location_list("michael", "city"),
            get_cities_for_dropdown(),
        ),
        (
            "Capitols",
            "capitol",
            get_top_ten_capitol_list("joel"),
            get_top_ten_capitol_list("michael"),
            get_capitols(),
        ),
        (
            "Parks",
            "national park",
            get_top_ten_location_list("joel", "national park"),
            get_top_ten_location_list("michael", "national park"),
            get_national_parks(),
        ),
        (
            "City Halls",
            "city hall",
            get_top_ten_location_list("joel", "city hall"),
            get_top_ten_location_list("michael", "city hall"),
            get_cityhalls(),
        ),
        (
            "Libaries",
            "library",
            get_top_ten_location_list("joel", "library"),
            get_top_ten_location_list("michael", "library"),
            get_libraries(),
        ),
        (
            "Museums",
            "museum",
            get_top_ten_location_list("joel", "museum"),
            get_top_ten_location_list("michael", "museum"),
            get_museums(),
        ),
        (
            "Buildings",
            "building",
            get_top_ten_location_list("joel", "building"),
            get_top_ten_location_list("michael", "building"),
            get_buildings(),
        ),
        (
            "Cities To Move To",
            "move to",
            get_top_ten_location_list("joel", "move to"),
            get_top_ten_location_list("michael", "move to"),
            get_cities_for_dropdown(),
        ),
        (
            "Canadian Railway Hotels",
            "canadian railway hotel",
            get_top_ten_canadian_railway_hotel_list("joel"),
            get_top_ten_canadian_railway_hotel_list("michael"),
            get_canadian_railway_hotels_for_dropdown(),
        ),
        (
            "Theatres",
            "theatre",
            get_top_ten_theatres_list("joel"),
            get_top_ten_theatres_list("michael"),
            get_theatres_for_app(),
        ),
        (
            "Quaker Meetings",
            "quaker",
            get_top_ten_quaker_meeting_list("joel"),
            get_top_ten_quaker_meeting_list("michael"),
            get_quaker_meetings_for_dropdown(),
        ),
    ]

    return templates.TemplateResponse(
        request=request,
        name="admin/update_top_ten.html",
        context={"cities": get_cities_for_dropdown(), "top_ten_lists": top_ten_lists},
    )


@router.post("/add_visit")
def add_visit(
    location_type: int = Form(...),
    location_id: str = Form(...),
    visit_date: str = Form(...),
    new_location_name: str = Form(""),
    new_state: str = Form(""),
    new_country: str = Form("USA"),
    new_latitude: str = Form(""),
    new_longitude: str = Form(""),
):
    print(f"Location Type: {location_type}")
    print(f"Location ID: {location_id}")
    print(f"Visit Date: {visit_date}")

    print(f"New Name: {new_location_name}")
    print(f"State: {new_state}")
    print(f"Country: {new_country}")

    next_visit_order = None
    if location_id == "new":
        location_id = create_location(
            name=new_location_name,
            location_type_id=location_type,
            state_province=new_state,
            country=new_country,
            latitude=new_latitude,
            longitude=new_longitude,
        )

        print(f"New location created with id = {location_id}")
        next_visit_order = get_next_visit_order()
        print(f"Next visit order = {next_visit_order}")
        create_location_rating(location_id)

    next_visit_number = get_next_visit_number()
    print(f"Next visit number = {next_visit_number}")

    visit_id = create_visit(
        location_id=location_id,
        visit_date=visit_date,
        visit_number=next_visit_number,
        visit_order=next_visit_order,
    )

    print(f"Visit created with id = {visit_id}")

    return RedirectResponse(url="/admin/home?success=visit_added", status_code=303)


class VisitAddition(BaseModel):
    location_id: int
    visit_date: str


@router.post("/add_visit_from_app")
def add_visit_from_app(visit: VisitAddition):

    print(f"Location ID: {visit.location_id}")
    print(f"Visit Date: {visit.visit_date}")

    next_visit_order = None

    next_visit_number = get_next_visit_number()
    print(f"Next visit number = {next_visit_number}")

    visit_id = create_visit(
        location_id=visit.location_id,
        visit_date=visit.visit_date,
        visit_number=next_visit_number,
        visit_order=next_visit_order,
    )

    print(f"Visit created with id = {visit_id}")

    return RedirectResponse(url="/admin/home?success=visit_added", status_code=303)


@router.get("/add_theatre")
def add_theatre_page(request: Request):
    try:
        user = require_admin(request)
    except Exception:
        return RedirectResponse("/login")

    visits = get_visits_for_dropdown()
    theatres = get_all_theatres_data()

    return templates.TemplateResponse(
        request=request,
        name="add_theatre.html",
        context={"visits": visits, "theatres": theatres},
    )


@router.post("/add_theatre")
def add_theatre(
    visit_id: int = Form(...),
    new_theatre_name: str = Form(...),
    new_address: str = Form(...),
    new_latitude: str = Form(""),
    new_longitude: str = Form(""),
    new_dresser: str = Form(""),
):
    print(f"Visit ID: {visit_id}")
    print(f"Theatre Name: {new_theatre_name}")
    print(f"Address: {new_address}")

    print(f"Latitude: {new_latitude}")
    print(f"Longitude: {new_longitude}")
    print(f"Dresser: {new_dresser}")

    next_theatre_number = get_next_theatre_number()
    print(f"Next theatre number = {next_theatre_number}")

    theatre_id = create_theatre(
        theatre_id=next_theatre_number,
        new_theatre_name=new_theatre_name,
        new_address=new_address,
        new_latitude=new_latitude,
        new_longitude=new_longitude,
        new_dresser=new_dresser,
    )

    add_theatre_to_visit(visit_id=visit_id, theatre_id=theatre_id)

    print(f"Visit [{visit_id}] updated with theatre id = {theatre_id}")

    return RedirectResponse(url="/admin/home?success=theatre_added", status_code=303)


@router.get("/add_digs")
def add_digs_page(request: Request):
    try:
        user = require_admin(request)
    except Exception:
        return RedirectResponse("/login")

    visits = get_visits_for_dropdown(without_digs=True)
    digs_types = get_digs_types()

    return templates.TemplateResponse(
        request=request,
        name="add_digs.html",
        context={"visits": visits, "digs_types": digs_types},
    )


@router.post("/add_digs")
def add_digs(
    visit_id: int = Form(...),
    digs_type: int = Form(...),
    new_address: str = Form(...),
    new_latitude: str = Form(""),
    new_longitude: str = Form(""),
    company_housing_bool: bool = Form("FALSE"),
):
    print(f"Visit ID: {visit_id}")
    print(f"Digs Type Num: {digs_type}")
    print(f"Address: {new_address}")

    print(f"Latitude: {new_latitude}")
    print(f"Longitude: {new_longitude}")
    print(f"Company Housing: {company_housing_bool}")

    next_digs_number = get_next_digs_number()
    print(f"Next digs number = {next_digs_number}")

    digs_id = create_digs(
        digs_id=next_digs_number,
        digs_type_id=digs_type,
        new_address=new_address,
        new_latitude=new_latitude,
        new_longitude=new_longitude,
        company_housing_bool=company_housing_bool,
    )

    add_digs_to_visit(visit_id=visit_id, digs_id=digs_id)

    print(f"Visit [{visit_id}] updated with digs id = {digs_id}")

    return RedirectResponse(url="/admin/home?success=digs_added", status_code=303)


@router.get("/add_location")
def add_location_page(request: Request):
    try:
        user = require_admin(request)
    except Exception:
        return RedirectResponse("/login")

    location_types = get_location_types()
    locations = get_locations_for_dropdown()

    return templates.TemplateResponse(
        request=request,
        name="add_location.html",
        context={"location_types": location_types, "locations": locations},
    )


@router.post("/add_location")
def add_location(
    location_type: int = Form(...),
    new_name: str = Form(...),
    new_state_province: str = Form(""),
    new_country: str = Form("USA"),
    new_latitude: str = Form(""),
    new_longitude: str = Form(""),
):
    print(f"Location Type: {location_type}")
    print(f"Name {new_name}")

    print(f"State: {new_state_province}")
    print(f"Country: {new_country}")
    print(f"Latitude: {new_latitude}")
    print(f"Longitude: {new_longitude}")

    new_id = create_location(
        name=new_name,
        location_type_id=location_type,
        state_province=new_state_province,
        country=new_country,
        latitude=new_latitude,
        longitude=new_longitude,
    )

    print(f"New location created with id = {new_id}")

    create_location_rating(new_id)
    print(f"New location rating created with id = {new_id}")

    if location_type in (5, 6, 7, 8):
        create_building_details(new_id)
        print(f"New buidling details created with id = {new_id}")

    return RedirectResponse(url="/admin/home?success=location_added", status_code=303)


class LocationAddition(BaseModel):
    location_type_id: int
    location_name: str
    state_province: str
    country: str
    latitude: float
    longitude: float


@router.post("/add_location_from_app")
def add_location_from_app(addition: LocationAddition):
    print(f"Location Type: {addition.location_type_id}")
    print(f"Name {addition.location_name}")

    print(f"State: {addition.state_province}")
    print(f"Country: {addition.country}")
    print(f"Latitude: {addition.latitude}")
    print(f"Longitude: {addition.longitude}")

    new_id = create_location(
        name=addition.location_name,
        location_type_id=addition.location_type_id,
        state_province=addition.state_province,
        country=addition.country,
        latitude=addition.latitude,
        longitude=addition.longitude,
    )

    print(f"New location created with id = {new_id}")

    create_location_rating(new_id)
    print(f"New location rating created with id = {new_id}")

    if addition.location_type_id in (5, 6, 7, 8):
        create_building_details(new_id)
        print(f"New buidling details created with id = {new_id}")

    return {"status": "ok", "location_id": new_id}
