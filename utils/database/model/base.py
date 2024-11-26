from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from core.settings import dbconfigs


url = f"postgresql+asyncpg://{dbconfigs.db_login}:{dbconfigs.db_pass}@{dbconfigs.db_host}/{dbconfigs.db_name}"
engine = create_async_engine(url, echo=True)
async_session = async_sessionmaker(engine)
metadata_obj = MetaData()

async def connectdb():
    async with engine.begin() as conn:
        await conn.run_sync(metadata_obj.create_all())