from sqlalchemy import Table, Column, ForeignKey, Integer
from base import metadata_obj

symbol = Table(
    "symbols",
    metadata_obj,
    Column("pk_id", Integer, primary_key=True),
    Column("users_id", Integer, ForeignKey("users.user_id"))
)