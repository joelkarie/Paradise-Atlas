from fastapi import APIRouter
from ..services.michael_could_live_service import get_michael_could_live

router = APIRouter(prefix="/michael-could-live", tags=["Places Michael Could Live"])


@router.get("")
def michael_could_live():
    return get_michael_could_live()
