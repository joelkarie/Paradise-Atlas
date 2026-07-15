from fastapi import APIRouter
from api.services.patagonia_services import get_patagonia_stores

router = APIRouter(prefix="/patagonia", tags=["Patagonia"])


@router.get("")
def patagonia_stores():
    return get_patagonia_stores()
