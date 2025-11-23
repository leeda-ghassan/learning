from sqlalchemy import Table, Column, Text, Integer, DateTime, Boolean
from sqlalchemy.dialects.postgresql import UUID
from src.database.execution import db_client


users = Table(
    "users",
    db_client.metadata,
    Column("id", UUID(as_uuid=True), primary_key=True, default=db_client.new_uuid),
    Column("username", Text),
    Column("email", Text, unique=True),
    Column("password", Text),
    Column("phone", Integer, nullable=False),
    Column("age", Integer, nullable=False),
    Column("major", Text, nullable=False),
    Column("experience", Text, nullable=False),
    Column("level", Text, nullable=False),
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


# model_performance = Table(
#     "model_performance",
#     db_client.metadata,
#     Column("id", UUID(as_uuid=True), primary_key=True, default=db_client.new_uuid),
#     Column("model_version", Text),
#     Column("accuracy", Text),
#     Column("fl_score", Integer),
#     Column("training_date", DateTime, nullable=False, **db_client.default_now),
#     Column("is_active", Boolean, default=True),
#     Column("created_at", DateTime, nullable=False, **db_client.default_now),
#     Column(
#         "updated_at",
#         DateTime,
#         nullable=False,
#         onupdate=db_client.now,
#         **db_client.default_now,
#     ),
# )
