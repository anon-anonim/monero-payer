from logging.config import dictConfig
import logging
import asyncpg
from fastapi import FastAPI

from .api.routes import router
from .settings import conf, API_PREFIX, LogConfig

dictConfig(LogConfig().dict())
log = logging.getLogger("monero-payer")

app = FastAPI()


@app.on_event("startup")
async def handle_startup():
    postgres_dsn = f"postgres://{conf.postgres_user}:{conf.postgres_password}@{conf.postgres_host}:{conf.postgres_port}/{conf.postgres_db}?sslmode={conf.postgres_sslmode}"
    pool = asyncpg.create_pool(dsn=postgres_dsn)
    log.info(f"Connected to Postgres on {conf.postgres_host}:{conf.postgres_port}")
    app.extra["db"] = pool


app.include_router(router, prefix=API_PREFIX)
