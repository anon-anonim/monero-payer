from fastapi import Request
from asyncpg.pool import Pool


def get_db_pool(request: Request) -> Pool:
    return request.app.extra['db']
