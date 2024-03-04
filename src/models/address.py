from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

from src.models.base import BaseModel


class Address(BaseModel):
    __tablename__ = "address"
    
    id:         Mapped[int]      = mapped_column(nullable=False, primary_key=True, autoincrement=True)    
    created_at: Mapped[datetime] = mapped_column(nullable=False, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(nullable=False, server_default=func.now())
    
    zip_code:     Mapped[str]      = mapped_column(nullable=False, unique=True)
    city:         Mapped[str]      = mapped_column(nullable=False)
    state:        Mapped[str]      = mapped_column(nullable=False) 
    street:       Mapped[str]      = mapped_column(nullable=True)
    neighborhood: Mapped[str]      = mapped_column(nullable=True)