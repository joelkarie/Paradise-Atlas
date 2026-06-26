from fastapi import APIRouter
from ..services.together_could_live_services import get_together_could_live

router = APIRouter(prefix="/together-could-live", tags=["We Both Could Live"])


@router.get("")
def michael_could_live():
    return get_together_could_live()
