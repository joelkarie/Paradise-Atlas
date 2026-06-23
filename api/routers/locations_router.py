from fastapi import APIRouter
from ..services.locations_services import get_locations

router = APIRouter(prefix="/locations", tags=["Locations"])


@router.get("")
def locations():
    return get_locations()
