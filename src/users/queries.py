from sqlalchemy import (
    select,
    insert,
    update,
    delete,
)
from src.users.schemas import users
from src.authentication.hash import HashHelper
from src.database.execution import db_client
from src.users.models import UserRequest, UserUpdate
from uuid import UUID


class UserQueries:
    def __init__(self):
        self.db_client = db_client
        self.hash_helper = HashHelper()

    def create_user(self, user_data: UserRequest):
        data = dict(user_data.model_dump(exclude_unset=True))
        data["password"] = self.hash_helper.hash_password(data["password"])
        stmt = insert(users).values(**data).returning(users)
        result = self.db_client.execute_one(stmt)
        return result

    def get_user_by_id(self, user_id: UUID):
        stmt = select(users).where(users.c.id == user_id)
        result = self.db_client.execute_one(stmt)
        return result

    def get_user_by_email(self, email: str):
        stmt = select(users).where(users.c.email == email)
        result = self.db_client.execute_one(stmt)
        return result

    def update_user_by_id(self, user_id: UUID, update_data: UserUpdate):
        stmt = (
            update(users)
            .where(users.c.id == user_id)
            .values(**update_data)
            .returning(users)
        )
        result = self.db_client.execute_one(stmt)
        return result

    def delete_user_by_id(self, user_id: UUID):
        stmt = delete(users).where(users.c.id == user_id).returning(users)
        result = self.db_client.execute_one(stmt)
        return result
