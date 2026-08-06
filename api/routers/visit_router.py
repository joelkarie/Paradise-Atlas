from fastapi import APIRouter
from api.services.visit_services import get_visit_order, get_journey

router = APIRouter(prefix="/visit", tags=["Visit"])


@router.get("/visit_order")
def visit_order():
    return get_visit_order()

@router.get("/journey")
def journey():
    return get_journey()