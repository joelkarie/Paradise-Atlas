from fastapi import APIRouter
from ..services.visit_services import get_visit_order

router = APIRouter(prefix="/visit", tags=["Visit"])


@router.get("/visit_order")
def visit_order():
    return get_visit_order()
