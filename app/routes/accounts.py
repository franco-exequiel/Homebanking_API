from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.database import get_async_session
from app.schemas.account import AccountCreate, AccountOut
from app.models.account import Account
from app.models.user import User

router = APIRouter()

@router.post("/", response_model=AccountOut)
async def create_account(account_data: AccountCreate, session: AsyncSession = Depends(get_async_session)):
    # Verificar que el usuario exista
    user = await session.get(User, account_data.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    # Validar que no tenga ya una cuenta en esa moneda
    result = await session.execute(
        select(Account).where(Account.user_id == user.id, Account.currency == account_data.currency.upper())
    )
    if result.scalars().first():
        raise HTTPException(status_code=400, detail="Ya existe una cuenta en esa moneda")

    account = Account(
        user_id=user.id,
        currency=account_data.currency.upper(),
        balance=account_data.balance,
    )
    session.add(account)
    await session.commit()
    await session.refresh(account)
    return account