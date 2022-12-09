from typing import List

from asyncpg import Connection
from fastapi import Depends, FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.routing import APIRoute

from .auth import get_current_user
from .database import get_db
from .models import Game, Player, PlayerScore, PlayerStatus, PlayerStatusPatch, User

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def healthcheck():
    return "ok"


@app.get("/games", response_model=List[Game])
def get_games(user: User = Depends(get_current_user), db: Connection = Depends(get_db)):
    """Get the current user's games."""
    raise NotImplementedError()


@app.post("/games", status_code=status.HTTP_201_CREATED, response_model=Game)
def create_game(
    user: User = Depends(get_current_user),
    db: Connection = Depends(get_db),
):
    """Create a new game owned by the current user."""
    raise NotImplementedError()


@app.post("/games/{gid}/join-request", status_code=status.HTTP_204_NO_CONTENT)
def create_join_request(
    gid: str, user: User = Depends(get_current_user), db: Connection = Depends(get_db)
):
    """Create a new join request for a given game."""


@app.get("/games/{gid}/my-status", response_model=PlayerStatus)
def get_my_status(
    gid: str, user: User = Depends(get_current_user), db: Connection = Depends(get_db)
):
    """Get the current user's status in a given game."""
    return PlayerStatus(is_active=False, has_hunter=False, prey_name=None)


@app.patch("/games/{gid}/my-status", status_code=status.HTTP_204_NO_CONTENT)
def patch_my_status(
    gid: str,
    patch: PlayerStatusPatch,
    user: User = Depends(get_current_user),
    db: Connection = Depends(get_db),
):
    """Update the current user's status in a given game."""
    return "ok"


@app.get("/games/{gid}/scores", response_model=List[PlayerScore])
def get_scores(
    gid: str, user: User = Depends(get_current_user), db: Connection = Depends(get_db)
):
    """Get the current user's status in a given game."""
    return []


@app.post("/games/{gid}/assassinations", status_code=status.HTTP_204_NO_CONTENT)
def create_assassination(
    gid: str, user: User = Depends(get_current_user), db: Connection = Depends(get_db)
):
    """Record an assassination of the current user."""
    return "ok"


@app.get("/games/{gid}/admin/players", response_model=List[Player])
def get_players(
    gid: int,
    user: User = Depends(get_current_user),
    db: Connection = Depends(get_db),
):
    """Get players in a given game. Only callable by game owner."""
    return []


@app.delete("/games/{gid}/admin/players/{pid}", status_code=status.HTTP_204_NO_CONTENT)
def delete_player(
    gid: int,
    pid: int,
    user: User = Depends(get_current_user),
    db: Connection = Depends(get_db),
):
    """Remove a given player from the game. Only callable by game owner."""


@app.post(
    "/games/{gid}/admin/players/{pid}/approval", status_code=status.HTTP_204_NO_CONTENT
)
def approve_player(
    gid: int,
    pid: int,
    user: User = Depends(get_current_user),
    db: Connection = Depends(get_db),
):
    """Get players in a given game. Only callable by game owner."""
    return []


@app.post("/games/{gid}/admin/archive", status_code=status.HTTP_204_NO_CONTENT)
def archive_game(
    gid: int,
    user: User = Depends(get_current_user),
    db: Connection = Depends(get_db),
):
    """Archive a given game. Only callable by game owner."""


for route in app.routes:
    if isinstance(route, APIRoute):
        route.operation_id = route.name
