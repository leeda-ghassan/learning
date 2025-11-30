from uuid import UUID
from src.skills.models import SkillCreate, SkillResponse, SkillUpdate
from src.skills.queries import SkillQueries


class SkillsService:
    def __init__(self):
        self.skills_queries = SkillQueries()

    def get_skills(self):
        try:
            rows = self.skills_queries.list_skills()
            if not rows:
                return None
            skill_list = [SkillResponse(**dict(r)) for r in rows]
            return skill_list
        except Exception as e:
            print(f"Error fetching skills: {e}")
            return None

    def get_skill_by_id(self, skill_id: UUID):
        try:
            row = self.skills_queries.get_skill_by_id(skill_id)
            if not row:
                return None
            skill_data = SkillResponse(**dict(row))
            return skill_data
        except Exception as e:
            print(f"Error fetching skill by id: {e}")
            return None

    def create_skill(self, skill_data: SkillCreate):
        try:
            existing = self.skills_queries.get_skill_by_name(skill_data.name)
            if existing:
                return 500, None
            row = self.skills_queries.create_skill(skill_data)
            if not row:
                return 400, None
            skill_data_resp: SkillResponse = SkillResponse(**dict(row))
            return 200, skill_data_resp
        except Exception as e:
            print(f"Error creating skill: {e}")
            return 400, None

    def update_skill(self, skill_id: UUID, update_data: SkillUpdate):
        try:
            row = self.skills_queries.update_skill_by_id(skill_id, update_data)
            if not row:
                return None
            skill_data: SkillResponse = SkillResponse(**dict(row))
            return skill_data
        except Exception as e:
            print(f"Error updating skill: {e}")
            return None

    def delete_skill(self, skill_id: UUID):
        try:
            row = self.skills_queries.delete_skill_by_id(skill_id)
            if not row:
                return None
            skill_data: SkillResponse = SkillResponse(**dict(row))
            return skill_data
        except Exception as e:
            print(f"Error deleting skill: {e}")
            return None