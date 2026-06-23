from fastapi import APIRouter
from ..services.capitols_services import get_capitols

router = APIRouter(prefix="/capitols", tags=["Capitols"])


@router.get("")
def capitols():
    return get_capitols()
