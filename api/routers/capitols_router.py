from fastapi import APIRouter
from api.services.capitols_services import get_capitols

router = APIRouter(prefix="/capitols", tags=["Capitols Visited"])


@router.get("")
def capitols():
    return get_capitols()
