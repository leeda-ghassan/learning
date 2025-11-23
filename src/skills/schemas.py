from sqlalchemy import Table, Column, Text, Integer, DateTime, Boolean
from sqlalchemy.dialects.postgresql import UUID
from src.database.execution import db_client

skills = Table(
    "skills",
    db_client.metadata,
    Column("id", UUID(as_uuid=True), primary_key=True, default=db_client.new_uuid),
    Column("name", Text),
    Column("description", Text, unique=True),
    Column("created_at", DateTime, nullable=False, **db_client.default_now),
    Column(
        "updated_at",
        DateTime,
        nullable=False,
        onupdate=db_client.now,
        **db_client.default_now,
    ),
)
