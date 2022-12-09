import asyncio
import functools
import importlib.resources

import aiosql
import asyncpg

from .config import get_settings


async def get_connection_pool():
    settings = get_settings()
    return await asyncpg.create_pool(
        host=settings.pghost,
        port=settings.pgport,
        user=settings.pguser,
        password=settings.pgpassword,
        database=settings.pgdatabase,
    )


async def get_db():
    pool = await get_connection_pool()
    conn = await pool.acquire()
    try:
        yield
    finally:
        await conn.close()


queries = aiosql.from_path(
    importlib.resources.path("backend", "queries.sql"), "asyncpg"
)
