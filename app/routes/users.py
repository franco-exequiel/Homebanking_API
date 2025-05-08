from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.database import get_async_session
from app.schemas.user import UserCreate, UserOut
from app.schemas.account import AccountOut
from app.models.user import User
from app.models.account import Account
from app.services.auth import hash_password

router = APIRouter()

@router.post("/", response_model=UserOut)
async def create_user(user_data: UserCreate, session: AsyncSession = Depends(get_async_session)):
    try:
        # Validar email y DNI únicos
        result = await session.execute(
            select(User).where((User.email == user_data.email) | (User.dni == user_data.dni))
        )
        existing = result.scalars().first()
        if existing:
            raise HTTPException(status_code=400, detail="Email o DNI ya registrados")

        # Crear usuario
        user = User(
            name=user_data.name,
            email=user_data.email,
            dni=user_data.dni,
            hashed_password=hash_password(user_data.password),
        )
        session.add(user)
        await session.flush()  # obtener user.id antes de crear cuenta

        # Crear cuenta inicial en ARS
        account = Account(user_id=user.id, currency="ARS", balance=0.0)
        session.add(account)

        await session.commit()
        return user

    except Exception as e:
        import traceback
        traceback.print_exc()  # Muestra el error completo en consola
        raise HTTPException(status_code=500, detail=str(e))