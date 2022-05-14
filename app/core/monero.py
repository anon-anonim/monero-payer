import logging

from asyncpg.pool import Pool

import asyncpg

log = logging.getLogger("monero-payer")

from monero.wallet import Wallet

from monero.backends.jsonrpc import JSONRPCWallet


# async def get_address(pool: Pool):
#     log.debug(f"{pool=}")
#     w = Wallet(JSONRPCWallet(port=18082))
#     mn_adrs = 'ОСНОВНОЙ АДРЕСС- '+str(w.address())
#     #mn_acc = 'АККАУНТ- '+str(w.accounts[0])
#     #new_adrs = 'НОВЫЙ АДРЕСС- '+str(w.accounts[0].new_address())
#     #sub_adrs_all = 'СПИСОК АДРЕСОВ НА АККАУНТЕ' + str(w.accounts[0].addresses())
#     #amt_sub_adrs = 'КОЛИЧЕСТВО АДРЕСОВ НА АККАУНТЕ ' + str(len(w.accounts[0].addresses()))
#     return (mn_adrs)
# bd_cnct = await asyncpg.connect('postgresql://postgres:postgres@localhost:5432/monero-payer')
# log.debug(f"{pool=}")

async def get_address(pool: Pool) -> str:
    
    async with pool.acquire() as bd_cnct:
        dct_adrs = await bd_cnct.fetchrow ('''select address from accounts where in_use = False ''') # получаем 1 строку в виде словаря
        if dct_adrs != None:
            get_adrs = dct_adrs.get('address')
        else:            
            w = Wallet(JSONRPCWallet(port=18082))
            nw_adrs = str((w.accounts[0].new_address())[0]) # получаем кортеж с адресом субкошелька и его порядковым номером обрезаем
            async with bd_cnct.transaction():    
                await bd_cnct.execute('''insert into accounts (address) values( $1 )''', nw_adrs )
            get_adrs = nw_adrs
        async with bd_cnct.transaction():
            await bd_cnct.execute(''' update accounts set in_use = True where address = $1 ''', get_adrs ) # адрес отмечается как используемый
        return (get_adrs)


async def check_transaction(
    pool: Pool,
    wallet_address: str,
    transaction_id: str,
    amount: int,
) -> bool:
    log.debug(f"{pool=}")
    log.debug(f"{wallet_address=}")
    log.debug(f"{transaction_id=}")
    return False


async def get_wallet_transactions(
    pool: Pool,
    wallet_address: str,
):
    log.debug(f"{pool=}")
    log.debug(f"{wallet_address=}")
    return []