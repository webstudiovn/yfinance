from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base

class Symbol(Base):
    __tablename__ = "symbols"
    pk_id: Mapped[int] = mapped_column(primary_key=True)
    users_id: Mapped[int] = mapped_column(ForeignKey("users.pk_id"))