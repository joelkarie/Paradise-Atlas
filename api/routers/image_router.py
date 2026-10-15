from pathlib import Path
from fastapi.responses import JSONResponse
from fastapi import APIRouter, UploadFile, File, HTTPException, Form

from api.services.github_service import GithubService
from api.services.image_service import ImageService
from api.services.image_paths import ImagePaths

router = APIRouter(prefix="/images", tags=["Images"])


@router.post("/admin/add_image/{type_name}/{type_id}/image")
async def upload_image(type_name: str, type_id: int, file: UploadFile = File(...)):
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


@router.post("/admin/add_images_batch/{type_name}")
async def upload_images_batch(
    type_name: str,
    files: list[UploadFile] = File(...),
    ids: list[int] = Form(...),
):
    if not files:
        raise HTTPException(
            status_code=400,
            detail="Please select at least one image.",
        )

    if len(files) != len(ids):
        raise HTTPException(
            status_code=400,
            detail="Each image must have a corresponding record ID.",
        )

    if len(set(ids)) != len(ids):
        raise HTTPException(
            status_code=400,
            detail="Each record ID can only appear once in a batch.",
        )

    github = GithubService()
    batch_files = []

    for file, type_id in zip(files, ids):
        if not (file.content_type or "").startswith("image/"):
            raise HTTPException(
                status_code=400,
                detail=f"{file.filename} is not an image.",
            )

        image_bytes = await file.read()
        optimized = ImageService.optimize(image_bytes)

        batch_files.append({
            "path": ImagePaths.type_id(type_name, type_id),
            "content": optimized,
        })

    try:
        result = github.upload_files_batch(
            files=batch_files,
            commit_message=(
                f"Batch upload: {len(batch_files)} "
                f"{type_name} images"
            ),
        )
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Batch upload failed: {str(exc)}",
        ) from exc

    return result
