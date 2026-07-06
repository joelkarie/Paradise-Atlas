from fastapi import APIRouter
from ..services.digs_services import get_housing_distances, get_digs_types

router = APIRouter(prefix="/digs", tags=["Digs"])


@router.get("")
def housing_distances():
    return get_housing_distances()


@router.get("/digs_types")
def digs_types():
    return get_digs_types()
