import asyncio
from app.database import engine, Base
from app.models import user, account

async def init_models():
    async with engine.begin() as conn:
        print("📦 Creando tablas...")
        await conn.run_sync(Base.metadata.drop_all)  # opcional: limpia la DB
        await conn.run_sync(Base.metadata.create_all)
        print("✅ Tablas creadas exitosamente.")

if __name__ == "__main__":
    asyncio.run(init_models())