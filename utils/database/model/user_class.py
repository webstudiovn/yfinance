from typing import List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import BigInteger, String

from .base import Base
from .symbol_class import Symbol

class User(Base):
    __tablename__ = "users"
    pk_id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[BigInteger] = mapped_column(BigInteger)
    symbol: Mapped[str] = mapped_column(String(20))
    sheet_id: Mapped[str] = mapped_column(String(200), nullable=True)
    user_id: Mapped[List["Symbol"]] = relationship()