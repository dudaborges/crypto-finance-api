from asyncio import run

from database.connection import engine
from database.models import Base

async def create_database():
    # begin inicia a transação ao db
    async with engine.begin() as connection:
        # roda de forma assíncrona
        await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)

if __name__ == '__main__':
    run(create_database())