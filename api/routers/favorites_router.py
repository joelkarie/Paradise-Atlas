from fastapi import APIRouter
from api.services.favorites_services import get_favorite_list

router = APIRouter(prefix="/favorites", tags=["Favorites"])


@router.get("/{column}/{topic}")
def favorite_list(column, topic):
    return get_favorite_list(column, topic)
