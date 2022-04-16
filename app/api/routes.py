from fastapi import APIRouter, Depends
from asyncpg.pool import Pool

from .dependencies import get_db_pool
from ..core import monero

router = APIRouter()


@router.get("/get_address")
async def get_address_route(pool: Pool = Depends(get_db_pool)):
    return await monero.get_address(pool)


@router.get("/check_transaction")
async def check_transaction_route(
    wallet_address: str,
    amount: int,
    pool: Pool = Depends(get_db_pool)
):
    return await monero.check_transaction(
        pool,
        wallet_address,
        amount,
    )


@router.get("/get_transactions/{wallet_address}")
async def get_wallet_transactions_route(
    wallet_address: str,
    pool: Pool = Depends(get_db_pool)
):
    return await monero.get_wallet_transactions(
        pool,
        wallet_address,
    )
