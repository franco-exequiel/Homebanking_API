from pydantic import BaseModel, Field

class AccountCreate(BaseModel):
    currency: str = Field(..., min_length=3, max_length=3)
    balance: float = Field(default=0.0, ge=0.0)

class AccountOut(BaseModel):
    id: int
    user_id: int
    currency: str
    balance: float

    class Config:
        from_attributes = True