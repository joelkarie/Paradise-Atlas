from fastapi import APIRouter
from ..services.canadian_railway_hotel_services import get_canadian_railway_hotels

router = APIRouter(prefix="/canadian_railway_hotels", tags=["Canadian Railway Hotels"])


@router.get("")
def canadian_railway_hotels():
    return get_canadian_railway_hotels(get_visited=False)

@router.get("/visited")
def visited_canadian_railway_hotels():
    return get_canadian_railway_hotels(get_visited=True)
