from sqlalchemy import select, insert, update, delete
from src.courses.schemas import course
from src.database.execution import db_client
from src.courses.models import CourseCreate, CourseUpdate
from uuid import UUID

class CourseQueries:
    def __init__(self):
        self.db_client = db_client

    def create_course(self, course_data: CourseCreate):
        row = (
            insert(course)
            .values(dict(course_data.model_dump(exclude_unset=True)))
            .returning(course)
        )
        result = self.db_client.execute_one(row)
        return result    

    def get_course_by_id(self, course_id: UUID):
        row = select(course).where(course.c.id == course_id)
        result = self.db_client.execute_one(row)
        return result

    def get_course_by_title(self, title: str):
        row = select(course).where(course.c.title == title)
        result = self.db_client.execute_one(row)
        return result

    def update_course_by_id(self, course_id: UUID, course_data: CourseUpdate):
        row = (
            update(course)
            #.values(dict(course_data.model_dump(exclude_unset=True)))
            .course_data: CourseResponse = CourseResponse(**dict(course))
            .where(course.c.id == course_id)
            .returning(course)
        )
        result = self.db_client.execute_one(row)
        return result
    
    def delete_course_by_id(self, course_id: UUID):
        row = (
            delete(course)
            .where(course.c.id == course_id)
            .returning(course)
        )
        result = self.db_client.execute_one(row)
        return result    

    def list_courses(self):
        row = select(course)
        result = self.db_client.execute_all(row)
        return result
    


