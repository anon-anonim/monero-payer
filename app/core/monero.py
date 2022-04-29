import logging

from asyncpg.pool import Pool


log = logging.getLogger("monero-payer")

from monero.wallet import Wallet

from monero.backends.jsonrpc import JSONRPCWallet


async def get_address(pool: Pool):
    log.debug(f"{pool=}")
    w = Wallet(JSONRPCWallet(port=18082))
    mn_adrs = 'ОСНОВНОЙ АДРЕСС- '+str(w.address())
    mn_acc = 'АККАУНТ- '+str(w.accounts[0])
    #new_adrs = 'НОВЫЙ АДРЕСС- '+str(w.accounts[0].new_address())
    sub_adrs_all = 'СПИСОК АДРЕСОВ НА АККАУНТЕ' + str(w.accounts[0].addresses())
    amt_sub_adrs = 'КОЛИЧЕСТВО АДРЕСОВ НА АККАУНТЕ - docker-compose up -d' + str(len(w.accounts[0].addresses()))
    return (mn_adrs, mn_acc, sub_adrs_all, amt_sub_adrs)


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
