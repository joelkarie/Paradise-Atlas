from fastapi import APIRouter, Request, Form
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from pathlib import Path

from api.auth import require_admin
from api.services.locations_services import (
    get_location_ratings,
    get_location_types,
    get_locations_for_dropdown,
    create_location,
    create_location_rating,
)
from api.services.visit_services import (
    get_next_visit_number,
    get_next_visit_order,
    create_visit,
    get_visits_for_dropdown,
    add_digs_to_visit,
)
from api.services.digs_services import get_digs_types, get_next_digs_number, create_digs

BASE_DIR = Path(__file__).resolve().parent.parent.parent

router = APIRouter(prefix="/admin")

templates = Jinja2Templates(directory="frontend/templates")


@router.get("/locations")
def admin_locations():
    return get_location_ratings()


@router.get("/home")
def admin_home_page(request: Request):
    try:
        user = require_admin(request)
    except Exception:
        return RedirectResponse("/login")

    return FileResponse(BASE_DIR / "frontend" / "admin_home.html")


@router.get("/joel")
def joel_admin_page(request: Request):
    try:
        user = require_admin(request)
    except Exception:
        return RedirectResponse("/login")

    return FileResponse(BASE_DIR / "frontend" / "joel_admin.html")


@router.get("/michael")
def michael_admin_page(request: Request):
    try:
        user = require_admin(request)
    except Exception:
        return RedirectResponse("/login")

    return FileResponse(BASE_DIR / "frontend" / "michael_admin.html")


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


@router.post("/add_visit")
def add_visit(
    location_type: int = Form(...),
    location_id: str = Form(...),
    visit_date: str = Form(...),
    new_location_name: str = Form(""),
    new_state: str = Form(""),
    new_country: str = Form("USA"),
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

    return {"success": True}


@router.get("/add_theatre")
def add_theatre_page(request: Request):
    try:
        user = require_admin(request)
    except Exception:
        return RedirectResponse("/login")

    visits = get_visits_for_dropdown()

    return templates.TemplateResponse(
        request=request,
        name="add_theatre.html",
        context={
            "visits": visits,
        },
    )


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

    return {"success": True}

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
