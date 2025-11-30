from sqlalchemy import select, insert, update, delete
from src.skills.schemas import skills
from src.database.execution import db_client
from src.skills.models import SkillCreate, SkillUpdate
from uuid import UUID


class SkillQueries:
    def __init__(self):
        self.db_client = db_client

    def create_skill(self, skill_data: SkillCreate):
        data = dict(skill_data.model_dump(exclude_unset=True))
        stmt = insert(skills).values(**data).returning(skills)
        result = self.db_client.execute_one(stmt)
        return result

    def get_skill_by_id(self, skill_id: UUID):
        stmt = select(skills).where(skills.c.id == skill_id)
        result = self.db_client.execute_one(stmt)
        return result

    def get_skill_by_name(self, name: str):
        stmt = select(skills).where(skills.c.name == name)
        result = self.db_client.execute_one(stmt)
        return result

    def update_skill_by_id(self, skill_id: UUID, update_data: SkillUpdate):
        data = dict(update_data.model_dump(exclude_unset=True))
        stmt = (
            update(skills)
            .where(skills.c.id == skill_id)
            .values(**data)
            .returning(skills)
        )
        result = self.db_client.execute_one(stmt)
        return result

    def delete_skill_by_id(self, skill_id: UUID):
        stmt = delete(skills).where(skills.c.id == skill_id).returning(skills)
        result = self.db_client.execute_one(stmt)
        return result

    def list_skills(self):
        stmt = select(skills)
        result = self.db_client.execute_all(stmt)
        return result