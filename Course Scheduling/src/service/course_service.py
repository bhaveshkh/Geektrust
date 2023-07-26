from src.core.exception import CourseExistsException
from src.core.utils import format_date
from src.models.course import Course
from collections import defaultdict


class CourseService:
    def __init__(self):
        self.courses = {}
        self.course_participants = defaultdict(set)

    def add_course_offering(self, course_name, instructor, date, min_employees, max_employees):

        # Create a course object and add it to available courses
        formatted_date = format_date(date)
        course = Course(course_name, instructor, formatted_date, int(min_employees), int(max_employees))
        course_id = course.get_course_id()

        if course_id in self.courses:
            raise CourseExistsException
        
        self.courses[course_id] = course
        return course_id

    def get_course_details(self, course_id):
        course_details = {}
        course_offering_ids = self.course_participants.get(course_id)
        course_details['course_name'] = self.courses[course_id].get_course_name()
        course_details['course_offering_ids'] = course_offering_ids
        course_details['instructor_name'] = self.courses[course_id].get_instructor_name()
        course_details['start_data'] = self.courses[course_id].get_start_date()

        return course_details

    def perform_course_allotment(self, course_id):
        course = self.courses.get(course_id)
        status = course.set_course_allotment_status()
        return status

    def is_valid_course_id(self, course_id):
        return course_id in self.courses.keys()

    def is_course_available(self, course_id):

        return self.courses[course_id].is_course_available()

    def add_employee_to_course(self, course_id, course_offering_id):
        self.course_participants[course_id].add(course_offering_id)
        self.courses[course_id].increase_registered_employees()

    def cancel_subscription(self, course_offering_id):
        course_id = None
        for _course_id in self.course_participants.keys():
            if course_offering_id in self.course_participants[_course_id]:
                course_id = _course_id

        course = self.courses.get(course_id)
        course_allotment_status = course.get_course_allotment_status()

        if course_allotment_status:
            return course_offering_id, "CANCEL_REJECTED"
        else:
            self.course_participants[course_id].remove(course_offering_id)
            return course_offering_id, "CANCEL_ACCEPTED"
