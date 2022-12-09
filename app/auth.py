from fastapi import Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from .models import User

security = HTTPBasic()


def get_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    return User(email=credentials.username)
