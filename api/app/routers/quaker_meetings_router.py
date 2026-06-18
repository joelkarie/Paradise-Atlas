from fastapi import APIRouter
from ..services.quaker_meeting_services import get_quaker_meetings

router = APIRouter(prefix="/quaker-meetings", tags=["Quaker Meetings"])


@router.get("")
def quaker_meetings():
    return get_quaker_meetings()
