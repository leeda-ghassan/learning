from uuid import UUID
from src.users.models import UserRequest
from src.users.queries import UserQueries


class UsersService:
    def __init__(self):
        self.users_queries = UserQueries()

    def create_user(self, user_data: UserRequest):
        row = self.users_queries.get_user_by_email(user_data.email)
        if row:
            return 500, None
        user = self.users_queries.create_user(user_data)
        if not user:
            return 400, None
        return 200, user

    def authenticate_user(self, email: str, password: str):
        user = self.users_queries.get_user_by_email(email)
        if not user:
            return None
        is_valid = self.users_queries.hash_helper.verify_password(
            password, user["password"]
        )
        if not is_valid:
            return None
        return user

    def get_profile(self, user_id: UUID):
        profiles = self.users_queries.get_user_by_id(user_id)
        if not profiles:
            return None

        return profiles

    def update_profile(self, profile_id: UUID, input_text: str):
        profile = self.users_queries.update_profile(profile_id, input_text)
        if not profile:
            return None

        return profile
