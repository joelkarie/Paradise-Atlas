from fastapi import APIRouter
from api.services.livable_services import (
    get_joel_livable_cities,
    get_michael_livable_city,
    get_joined_livable_cities,
)

router = APIRouter(prefix="/livable", tags=["Places We Could Live"])


@router.get("/joel")
def joel_livable_cities():
    return get_joel_livable_cities()


@router.get("/michael")
def michael_livable_cities():
    return get_michael_livable_city()


@router.get("/together")
def joined_livable_cities():
    return get_joined_livable_cities()
