from enum import Enum
from typing import Literal, Union

from pydantic import BaseModel, EmailStr


class User(BaseModel):
    email: EmailStr


class GameStatus(str, Enum):
    pending = "pending"
    joined = "joined"
    archived = "archived"


class Game(BaseModel):
    id: str
    status: GameStatus
    is_mine: bool


class GamePatch(BaseModel):
    name: str


class JoinRequest(BaseModel):
    username: str


class PlayerStatus(BaseModel):
    is_active: bool
    has_hunter: bool
    prey_name: str | None


class PlayerStatusPatch(BaseModel):
    is_participating: bool | None


class PlayerScore(BaseModel):
    id: int
    name: str
    score: int


class Player(BaseModel):
    id: EmailStr
    username: str
    is_approved: bool
