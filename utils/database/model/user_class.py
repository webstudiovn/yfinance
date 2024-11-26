from sqlalchemy import (Table, Column, Integer,
                        String, BigInteger)
from base import metadata_obj 

user = Table(
    "users",
    metadata_obj,
    Column("pk_id", Integer, primary_key=True),
    Column("user_id", Integer),
    Column("symbol", String),
    Column("sheet_id", BigInteger, nullable=True)
)