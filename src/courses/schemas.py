from sqlalchemy import Table, Column, Text, Integer, DateTime, Boolean
from sqlalchemy.dialects.postgresql import UUID
from src.database.execution import db_client


courses = Table(
    "courses",
    db_client.metadata,
    Column("id", UUID(as_uuid=True), primary_key=True, default=db_client.new_uuid),
    Column("title", Text),
    Column("description", Text),
    Column("instructor", Text),
    Column("duration", Integer, nullable=False),
    Column("level", Text, nullable=False),
    Column("time_interval", Text, nullable=False),
    Column("skill_requirements", Text, nullable=False),
    Column("last_login_at", DateTime, nullable=True, onupdate=db_client.now),
    Column("created_at", DateTime, nullable=False, **db_client.default_now),
    Column(
        "updated_at",
        DateTime,
        nullable=False,
        onupdate=db_client.now,
        **db_client.default_now,
    ),
)
