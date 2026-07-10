from pathlib import Path
from fastapi.responses import JSONResponse
from fastapi import APIRouter, UploadFile, File, HTTPException
from api.services.github_service import GithubService
from api.services.image_service import ImageService
from api.services.image_paths import ImagePaths

router = APIRouter(prefix="/images", tags=["Images"])





@router.post("/admin/add_image/{type_name}/{type_id}/image")
async def upload_image(type_name: str,type_id: int, file: UploadFile = File(...)):
    print("UPLOAD ROUTE HIT")
    print("TYPE:", type_name)
    print("TYPE ID:", type_id)
    print("FILE:", file.filename)    
    
    # TODO: Add check to make sure id exists in type table

    # Make sure it's an image
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image.")

    image_bytes = await file.read()

    optimized = ImageService.optimize(image_bytes)

    github = GithubService()

    result = github.upload_file(
        path=ImagePaths.type_id(type_name, type_id),
        content=optimized,
        commit_message=f"Updated {type_name} image #{type_id}",
    )

    return result