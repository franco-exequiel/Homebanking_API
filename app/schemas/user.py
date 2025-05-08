from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    dni: int = Field(..., ge=1000000, le=99999999)  # Entre 7 y 8 cifras
    password: str = Field(..., min_length=6)

class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    dni: str

    class Config:
        orm_mode = True