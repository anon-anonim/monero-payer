import os

from pydantic import BaseSettings, BaseModel


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
API_PREFIX: str = "/monero"


class Settings(BaseSettings):
    postgres_host: str = os.environ.get("POSRGRES_HOST", "localhost")
    postgres_user: str = os.environ.get("POSTGRES_USER", "postgres")
    postgres_password: str = os.environ.get("POSTGRES_PASSWORD", "postgres")
    postgres_port: str = os.environ.get("POSTGRES_PORT", "5432")
    postgres_db: str = os.environ.get("POSTGRES_DB", "monero-payer")
    postgres_sslmode: str = os.environ.get("POSTGRES_SSLMODE")

    class Config:
        env_prefix = ""
        env_file = ".env"
        env_file_encoding = "utf-8"


conf = Settings()


class LogConfig(BaseModel):
    """Logging configuration to be set for the server"""

    LOGGER_NAME: str = "monero-payer"
    LOG_FORMAT: str = "%(levelprefix)s | %(asctime)s | %(message)s"
    LOG_LEVEL: str = "DEBUG"

    # Logging config
    version = 1
    disable_existing_loggers = False
    formatters = {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": LOG_FORMAT,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    }
    handlers = {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
    }
    loggers = {
        "monero-payer": {"handlers": ["default"], "level": LOG_LEVEL},
    }
