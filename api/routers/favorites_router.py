from fastapi import APIRouter, HTTPException
from api.services.favorites_services import get_favorite_list
from sqlalchemy import text
from ..database import engine

router = APIRouter(prefix="/favorites", tags=["Favorites"])


@router.get("/{column}/{topic}")
def favorite_list(column, topic):
    return get_favorite_list(column, topic)


@router.put("/favorites/{column}/{name}/{position}/{location_id}")
async def replace_favorite_location(
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
        UPDATE favorites AS f
        SET {column} = (
            SELECT array_agg(
                CASE
                    WHEN s.i = :position THEN :location_id
                    ELSE f.{column}[s.i]
                END
                ORDER BY s.i
            )
            FROM generate_subscripts(f.{column}, 1) AS s(i)
        )
        WHERE f.name = :name
          AND array_length(f.{column}, 1) >= :position
        RETURNING f.{column}
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
                    detail="Favorites row not found or position is out of range"
                )

        return {
            "message": "Favorite location replaced successfully",
            "column": column,
            "name": name,
            "position": position,
            "location_id": location_id,
            "updated_favorites": updated_array
        }

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
