from fastapi import APIRouter
from ..services.joel_could_live_services import get_joel_could_live

router = APIRouter(prefix="/joel-could-live", tags=["Joel Could Live"])


@router.get("")
def joel_could_live():
    return get_joel_could_live()
