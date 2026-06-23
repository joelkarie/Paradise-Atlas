from fastapi import APIRouter
from ..services.theatre_services import get_theatres

router = APIRouter(prefix="/theatres", tags=["Theatres"])


@router.get("")
def theatres():
    return get_theatres()
