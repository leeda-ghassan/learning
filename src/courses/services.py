from uuid import UUID
from src.courses.models import CourseCreate, CourseResponse, CourseUpdate
from src.courses.queries import CourseQueries


class CoursesService:
    def __init__(self):
        self.courses_queries = CourseQueries()

    def get_courses(self):
        try:
            rows = self.courses_queries.list_courses()
            if not rows:
                return None
            course_list = [CourseResponse(**dict(r)) for r in rows]
            return course_list
        except Exception as e:
            print(f"Error fetching courses: {e}")
            return None

    def get_course_by_id(self, course_id: UUID):
        try:
            row = self.courses_queries.get_course_by_id(course_id)
            if not row:
                return None
            course_data = CourseResponse(**dict(row))
            return course_data
        except Exception as e:
            print(f"Error fetching course by id: {e}")
            return None

    def create_course(self, course_data: CourseCreate):
        try:
            existing = self.courses_queries.get_course_by_title(course_data.title)
            if existing:
                # mirror UsersService behavior on duplicates (status code + payload)
                return 500, None
            row = self.courses_queries.create_course(course_data)
            if not row:
                return 400, None
            course_data_resp: CourseResponse = CourseResponse(**dict(row))
            return 200, course_data_resp
        except Exception as e:
            print(f"Error creating course: {e}")
            return 400, None

    def update_course(self, course_id: UUID, update_data: CourseUpdate):
        try:
            row = self.courses_queries.update_course_by_id(course_id, update_data)
            if not row:
                return None
            course_data: CourseResponse = CourseResponse(**dict(row))
            return course_data
        except Exception as e:
            print(f"Error updating course: {e}")
            return None

    def delete_course(self, course_id: UUID):
        try:
            row = self.courses_queries.delete_course_by_id(course_id)
            if not row:
                return None
            course_data: CourseResponse = CourseResponse(**dict(row))
            return course_data
        except Exception as e:
            print(f"Error deleting course: {e}")
            return None