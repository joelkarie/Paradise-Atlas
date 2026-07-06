import os
from fastapi import APIRouter, Request
from fastapi.responses import FileResponse, RedirectResponse

from itsdangerous import URLSafeSerializer

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

router = APIRouter(prefix="/admin")

serializer = URLSafeSerializer(os.getenv("SECRET_KEY"), salt="session")

def require_admin(request: Request):
    token = request.cookies.get("session")

    if not token:
        raise Exception("NOT_AUTHORIZED")

    try:
        data = serializer.loads(token)
        return data.get("user")
    except Exception:
        raise Exception("NOT_AUTHORIZED")


@router.get("/home")
def admin_home_page(request: Request):
    try:
        user = require_admin(request)
    except Exception:
        return RedirectResponse("/login")

    return FileResponse(BASE_DIR / "frontend" / "admin_home.html")