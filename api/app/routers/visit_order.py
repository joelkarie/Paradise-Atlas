from fastapi import APIRouter
from ..services.visit_order_services import get_visit_order

router = APIRouter(prefix="/visit-order", tags=["Visit Order"])


@router.get("")
def visit_order():
    return get_visit_order()
