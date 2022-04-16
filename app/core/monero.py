import logging

from asyncpg.pool import Pool


log = logging.getLogger("monero-payer")


async def get_address(pool: Pool):
    log.debug(f"{pool=}")
    return "wallet address here"


async def check_transaction(
    pool: Pool,
    wallet_address: str,
    amount: int,
):
    log.debug(f"{pool=}")
    log.debug(f"{wallet_address=}")
    log.debug(f"{amount=}")
    return False


async def get_wallet_transactions(
    pool: Pool,
    wallet_address: str,
):
    log.debug(f"{pool=}")
    log.debug(f"{wallet_address=}")
    return []
