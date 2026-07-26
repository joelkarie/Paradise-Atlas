from fastapi import APIRouter
from api.services.capitols_services import get_capitols, get_capitols_for_app

router = APIRouter(prefix="/capitols", tags=["Capitols Visited"])


@router.get("")
def capitols():
    return get_capitols()

@router.get("/for_app")
def capitols_for_app():
    return get_capitols_for_app()

