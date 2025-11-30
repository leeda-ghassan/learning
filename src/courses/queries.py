from sqlalchemy import select, insert, update, delete
from src.courses.schemas import courses
from src.database.execution import db_client
from src.courses.models import CourseCreate, CourseUpdate
from uuid import UUID


class CourseQueries:
    def __init__(self):
        self.db_client = db_client

    def create_course(self, course_data: CourseCreate):
        data = dict(course_data.model_dump(exclude_unset=True))
        stmt = insert(courses).values(**data).returning(courses)
        result = self.db_client.execute_one(stmt)
        return result

    def get_course_by_id(self, course_id: UUID):
        stmt = select(courses).where(courses.c.id == course_id)
        result = self.db_client.execute_one(stmt)
        return result

    def get_course_by_title(self, title: str):
        stmt = select(courses).where(courses.c.title == title)
        result = self.db_client.execute_one(stmt)
        return result

    def update_course_by_id(self, course_id: UUID, course_data: CourseUpdate):
        data = dict(course_data.model_dump(exclude_unset=True))
        stmt = (
            update(courses)
            .where(courses.c.id == course_id)
            .values(**data)
            .returning(courses)
        )
        result = self.db_client.execute_one(stmt)
        return result

    def delete_course_by_id(self, course_id: UUID):
        stmt = delete(courses).where(courses.c.id == course_id).returning(courses)
        result = self.db_client.execute_one(stmt)
        return result

    def list_courses(self):
        stmt = select(courses)
        result = self.db_client.execute_all(stmt)
        return result