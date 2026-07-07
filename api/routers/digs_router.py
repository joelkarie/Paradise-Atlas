from fastapi import APIRouter
from ..services.digs_services import (
    get_housing_distances,
    get_digs_types,
    get_digs_for_map,
)

router = APIRouter(prefix="/digs", tags=["Digs"])


@router.get("")
def housing_distances():
    return get_housing_distances()


@router.get("/digs_types")
def digs_types():
    return get_digs_types()


@router.get("/digs_for_map")
def digs_for_map():
    return get_digs_for_map()
