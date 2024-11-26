from typing import TYPE_CHECKING
from sqlalchemy import insert
if TYPE_CHECKING:
    from model.base import engine
    from model.user_class import users

async def add_symbol_db(tg_id, symbol_name, sheet_id):
    req = insert(users).values(tg_id, symbol_name, sheet_id)
    async with engine.connect() as conn:
        await conn.execute(req)