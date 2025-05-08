from fastapi import FastAPI
from app.routes.users import router as users_router
from app.routes.accounts import router as accounts_router
import logging

app = FastAPI(title="Fintech API", version="0.1.0")
logging.basicConfig(level=logging.DEBUG)  # 👈 esto muestra más logs


# Registrar las rutas
app.include_router(users_router, prefix="/users", tags=["Users"])
app.include_router(accounts_router, prefix="/accounts", tags=["Accounts"])