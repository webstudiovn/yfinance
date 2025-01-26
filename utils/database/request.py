import asyncio
from sqlalchemy import select
from typing import Optional
from .model.user_class import User
from .model.base import session


# Добавление записи
async def add_user(**kwargs) -> Optional[User]:
    async with session as asyncsesion:
        stmt = User(**kwargs)
        asyncsesion.add(stmt)
        await session.commit()

# Выборка записей
async def select_users():
    async with session as asyncsesion:
        query = select(User).limit(5)
        result = await asyncsesion.execute(query)
        users = result.scalars().all()
        for user in users:
            print(f"tg id: {user.tg_id}, symbol: {user.symbol}")
        return users