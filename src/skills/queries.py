from sqlalchemy import select, insert, update, delete
from src.skills.schemas import skill
from src.database.execution import db_client
from src.skills.models import SkillCreate
from uuid import UUID

class SkillQueries:
    def __init__(self):
        self.db_client = db_client

    def create_skill(self, skill_data: SkillCreate):
        row = (
            insert(skill)
            .values(dict(skill_data.model_dump(exclude_unset=True)))
            .returning(skill)
        )
        result = self.db_client.execute_one(row)
        return result    

    def get_skill_by_id(self, skill_id: UUID):
        row = select(skill).where(skill.c.id == skill_id)
        result = self.db_client.execute_one(row)
        return result

    def get_skill_by_name(self, name: str):
        row = select(skill).where(skill.c.name == name)
        result = self.db_client.execute_one(row)
        return result

    def update_skill_by_id(self, skill_id: UUID):
        row = (
            update(skill)
            .where(skill.c.id == skill_id)
            .returning(skill)
        )
        result = self.db_client.execute_one(row)
        return result

    def delete_skill_by_id(self, skill_id: UUID):
        row = (
            delete(skill)
            .where(skill.c.id == skill_id)
            .returning(skill)
        )
        result = self.db_client.execute_one(row)
        return result    

    def list_skills(self):
        row = select(skill)
        result = self.db_client.execute_all(row)
        return result