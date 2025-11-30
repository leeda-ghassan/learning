from uuid import UUID
from sqlalchemy import delete, insert, select, update
from src.courses.models import CourseCreate, CourseResponse, CourseUpdate
from src.courses.queries import CourseQueries
from src.courses.schemas import courses as course


class CoursesService:
    def __init__(self):
        self.courses_queries = CourseQueries()

    def get_courses(self):
        try:
            courses = self.courses_queries.list_courses()
            if not courses:
                return None
            course_list = [
                CourseResponse(**dict(course)) for course in courses
            ]
            return course_list
        except Exception as e:
            print(f"Error fetching courses: {e}")
            return None
    

    def get_course_by_id(self, course_id: UUID):
        try:
            course = self.courses_queries.get_course_by_id(course_id)
            if not course:
                return None
            course_data = CourseResponse(**dict(course))
            return course_data
        except Exception as e:
            print(f"Error fetching course by id: {e}")
            return None

    def create_course(self, course_data: CourseCreate):
        try:
            course = self.courses_queries.create_course(course_data)
            if not course:
                return None
            course_data: CourseResponse = CourseResponse(**dict(course))
            return course_data
        except Exception as e:
            print(f"Error creating course: {e}")
            return None
        

    def update_course(self, course_data: CourseUpdate):
        try:
            course = self.courses_queries.update_course_by_id(course_data)
            if not course:
                return None
            course_data: CourseResponse = CourseResponse(**dict(course))
            return course_data
        except Exception as e:
            print(f"Error creating course: {e}")
            return None 

    def delete_course(self, course_id: UUID):
        try:
            course = self.courses_queries.delete_course_by_id(course_id)
            if not course:
                return None
            course_data: CourseResponse = CourseResponse(**dict(course))
            return course_data
        except Exception as e:
            print(f"Error creating course: {e}")
            return None 