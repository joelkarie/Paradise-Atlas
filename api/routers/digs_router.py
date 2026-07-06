from fastapi import APIRouter
from ..services.digs_services import get_housing_distances

router = APIRouter(prefix="/housing-distances", tags=["Housing Distances"])


@router.get("")
def housing_distances():
    return get_housing_distances()
