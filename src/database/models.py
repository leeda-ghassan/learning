from sqlalchemy import Table, Column, Text, DateTime, ForeignKey, Float
from sqlalchemy.dialects.postgresql import UUID, ARRAY
from src.database.connection import db_client


users = Table(
    "users",
    db_client.metadata,
    Column("id", UUID(as_uuid=True), primary_key=True, default=db_client.new_uuid, nullable=False),
    Column("name", Text, nullable=False),
    Column("email", Text, nullable=False, unique=True),
    Column("created_at", DateTime, nullable=False, **db_client.default_now),
    Column("updated_at", DateTime, nullable=False, onupdate=db_client.now, **db_client.default_now),
)


skills = Table(
    "skills",
    db_client.metadata,
    Column("id", UUID(as_uuid=True), primary_key=True, default=db_client.new_uuid, nullable=False),
    Column("skill_name", Text, nullable=False, unique=True),
    Column("created_at", DateTime, nullable=False, **db_client.default_now),
    Column("updated_at", DateTime, nullable=False, onupdate=db_client.now, **db_client.default_now),
)


courses = Table(
    "courses",
    db_client.metadata,
    Column("id", UUID(as_uuid=True), primary_key=True, default=db_client.new_uuid, nullable=False),
    Column("course_id", Text, nullable=False, unique=True),  # external course identifier
    Column("course_title", Text, nullable=False),
    Column("course_description", Text),
    Column("skill_tags", ARRAY(Text)),  # optional: store skill names from metadata
    Column("created_at", DateTime, nullable=False, **db_client.default_now),
    Column("updated_at", DateTime, nullable=False, onupdate=db_client.now, **db_client.default_now),
)


course_skills = Table(
    "course_skills",
    db_client.metadata,
    Column("course_id", UUID(as_uuid=True), ForeignKey("courses.id", ondelete="CASCADE"), primary_key=True),
    Column("skill_id", UUID(as_uuid=True), ForeignKey("skills.id", ondelete="CASCADE"), primary_key=True),
)


embeddings = Table(
    "embeddings",
    db_client.metadata,
    Column("id", UUID(as_uuid=True), primary_key=True, default=db_client.new_uuid, nullable=False),
    Column("object_type", Text, nullable=False),  # "course" or "skill" or "user"
    Column("object_id", UUID(as_uuid=True), nullable=False),  # FK to courses, skills, or users
    Column("vector", ARRAY(Float), nullable=False),  # embedding vector
    Column("created_at", DateTime, nullable=False, **db_client.default_now),
    Column("updated_at", DateTime, nullable=False, onupdate=db_client.now, **db_client.default_now),
)
