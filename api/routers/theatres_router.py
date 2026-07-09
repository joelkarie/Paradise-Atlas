from fastapi import APIRouter, UploadFile, File, HTTPException
from api.services.theatre_services import get_theatres
from api.services.github_service import GithubService
from api.services.image_service import ImageService
from api.services.image_paths import ImagePaths

router = APIRouter(prefix="/theatres", tags=["Theatres"])


@router.get("")
def theatres():
    return get_theatres()


@router.post("/admin/theatres/{theatre_id}/image")
async def upload_theatre_image(theatre_id: int, file: UploadFile = File(...)):
    # Make sure it's an image
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image.")

    image_bytes = await file.read()

    optimized = ImageService.optimize(image_bytes)

    github = GithubService()

    result = github.upload_file(
        path=ImagePaths.theatre(theatre_id),
        content=optimized,
        commit_message=f"Updated theatre image #{theatre_id}",
    )

    return result
