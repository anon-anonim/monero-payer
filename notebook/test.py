import asyncio
from time import sleep
import types
import asyncpg
import datetime
import tracemalloc
from asyncpg.pool import Pool
import logging
import asyncpg



log = logging.getLogger("monero-payer")

from monero.wallet import Wallet

from monero.backends.jsonrpc import JSONRPCWallet

# async def cnct():
#     conct = await asyncpg.connect('postgresql://postgres:postgres@localhost:5432/monero-payer')
#     con=conct
#     return con
    

async def my_request(pool: Pool):
    conct = await asyncpg.connect('postgresql://postgres:postgres@localhost:5432/monero-payer')
    dta = await conct.fetchrow (
        'select address from accounts where id = 1')
    if dta == None:
         log.debug(f"{pool=}")
         w = Wallet(JSONRPCWallet(port=18082))
         dta = 'НОВЫЙ АДРЕСС- '+str(w.accounts[0].new_address())
    return dta
    


#con = asyncio.get_event_loop().run_until_complete(cnct())

request = asyncio.get_event_loop().run_until_complete(my_request())

print(request)



