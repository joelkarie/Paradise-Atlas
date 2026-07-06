import os

from fastapi import Request

from itsdangerous import URLSafeSerializer
from pwdlib import PasswordHash


password_hash = PasswordHash.recommended()

serializer = URLSafeSerializer(os.getenv("SECRET_KEY"), salt="session")

def get_current_user(request: Request):
    token = request.cookies.get("session")

    if not token:
        return None

    try:
        data = serializer.loads(token)
        return data.get("user")
    except Exception:
        return None


def require_admin(request: Request):
    token = request.cookies.get("session")

    if not token:
        raise Exception("NOT_AUTHORIZED")

    try:
        data = serializer.loads(token)
        return data.get("user")
    except Exception:
        raise Exception("NOT_AUTHORIZED")