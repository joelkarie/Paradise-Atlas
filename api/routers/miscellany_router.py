from fastapi import APIRouter, HTTPException, Request
from fastapi.templating import Jinja2Templates
from api.services.miscellany_services import get_top_ten_location_list, get_top_ten_capitol_list
from sqlalchemy import text
from ..database import engine

router = APIRouter(prefix="/miscellany", tags=["Miscellany"])
templates = Jinja2Templates(directory="frontend/templates/miscellany")


@router.get("/{column}/{topic}")
def top_ten_list(column, topic):
    return get_top_ten_location_list(column, topic)

@router.get("/top_ten/capitol/{column}")
def top_ten_capitol_list(column):
    return get_top_ten_capitol_list(column)



@router.put("/miscellany/{column}/{name}/{position}/{location_id}")
async def replace_top_ten_location(
    column: str,
    name: str,
    position: int,
    location_id: int
):
    allowed_columns = {"joel", "michael"}

    if column not in allowed_columns:
        raise HTTPException(
            status_code=400,
            detail="Invalid column name"
        )

    if position < 1:
        raise HTTPException(
            status_code=400,
            detail="Position must be 1 or greater"
        )

    query = text(f"""
        UPDATE top_tens AS t
        SET {column} = (
            SELECT array_agg(
                CASE
                    WHEN s.i = :position THEN :location_id
                    ELSE t.{column}[s.i]
                END
                ORDER BY s.i
            )
            FROM generate_subscripts(t.{column}, 1) AS s(i)
        )
        WHERE t.name = :name
          AND array_length(t.{column}, 1) >= :position
        RETURNING t.{column}
    """)

    try:
        with engine.begin() as conn:
            result = conn.execute(
                query,
                {
                    "name": name,
                    "position": position,
                    "location_id": location_id
                }
            )

            updated_array = result.scalar_one_or_none()

            if updated_array is None:
                raise HTTPException(
                    status_code=404,
                    detail="Top Ten row not found or position is out of range"
                )

        return {
            "message": "Top Ten location replaced successfully",
            "column": column,
            "name": name,
            "position": position,
            "location_id": location_id,
            "updated_top_ten": updated_array
        }

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/home")
def miscellany_home_page(request: Request):

    joels_cities = get_top_ten_location_list("joel", "city")


    return templates.TemplateResponse(
        request=request,
        name="miscellany_home.html",
        context={
           "joel_cities": joels_cities
        },
    )