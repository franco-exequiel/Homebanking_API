from sqlalchemy import Column, Integer, Float, ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import relationship
from app.database import Base

class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    balance = Column(Float, default=0.0)
    currency = Column(String(3), nullable=False)  # Ej: ARS, USD, EUR

    __table_args__ = (
        UniqueConstraint("user_id", "currency", name="uix_user_currency"),
    )

    user = relationship("User", backref="accounts")