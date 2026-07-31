from fastapi import APIRouter
from api.services.patagonia_services import get_patagonia_stores, get_patagonia_for_apps

router = APIRouter(prefix="/patagonia", tags=["Patagonia"])


@router.get("")
def patagonia_stores():
    return get_patagonia_stores()

@router.get("/stores_for_app")
def patagonia_stores_for_app():
    return get_patagonia_for_apps()