import asyncio
import importlib.resources
import os
from functools import update_wrapper

import click

from .database import get_connection_pool


@click.group()
def cli():
    pass


@cli.command()
def start():
    os.system("poetry run uvicorn --reload backend.main:app")


@cli.command()
def format():
    os.system("poetry run autoflake8 && poetry run isort . && poetry run black .")


@cli.command()
def init_db():
    with importlib.resources.open_text("backend", "schema.sql") as s:

        async def executescript():
            pool = await get_connection_pool()
            async with pool.acquire(timeout=5) as conn:
                await conn.execute(s.read())

        asyncio.run(executescript())


if __name__ == "__main__":
    cli()
