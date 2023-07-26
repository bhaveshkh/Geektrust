from src.service.course_service import CourseService
from src.service.employee_service import EmployeeService
from src.core.exception import InvalidCourseIdException
from src.core.utils import get_unformatted_date
from src.core.constants import *


class CommandProcessor:
    def __init__(self):
        self.employee_service = EmployeeService()
        self.course_service = CourseService()
        self.command_map = {
            "ADD-COURSE-OFFERING": self.add_course_offering,
            "REGISTER": self.register,
            "ALLOT": self.allot_course,
            "CANCEL": self.cancel,
        }

    def process_command(self, command, *args):
        # print(command, *args)
        command_function = self.command_map.get(command)
        if command_function:
            command_function(*args)
        else:
            print(INVALID_COMMAND)

    def add_course_offering(self, *args):
        try:
            course_name, instructor, date, min_employee, max_employee = args
            course_id = self.course_service.add_course_offering(course_name, instructor, date, min_employee,
                                                                max_employee)
            print(course_id)
        except Exception:
            print(INPUT_DATA_ERROR)

    def register(self, *args):
        try:
            email, course_id = args

            # Check if course_id given is valid
            if not self.course_service.is_valid_course_id(course_id):
                raise InvalidCourseIdException

            # Check if course is full or allotted
            if not self.course_service.is_course_available(course_id):
                print(COURSE_FULL_ERROR)
                return

            course_offering_id = self.employee_service.register_employee(email, course_id)
            self.course_service.add_employee_to_course(course_id, course_offering_id)

            print(course_offering_id, ACCEPTED)

        except Exception:
            print(INPUT_DATA_ERROR)

    def allot_course(self, *args):
        course_id = args[0]
        course_status = None
        if self.course_service.perform_course_allotment(course_id):
            course_status = CONFIRMED
        else:
            course_status = COURSE_CANCELED
        course_details = self.course_service.get_course_details(course_id)

        output = []
        for course_offering_id in course_details['course_offering_ids']:
            employee_email = self.employee_service.get_employee_details(course_offering_id)
            unformatted_date = get_unformatted_date(course_details['start_data'])
            output.append([course_offering_id, employee_email, course_id, course_details['course_name'],
                           course_details['instructor_name'], unformatted_date, course_status])

        output.sort(key=lambda x: x[0])
        for details in output:
            print(*details)

    def cancel(self, *args):
        course_offering_id = args[0]

        course_offering_id, message = self.course_service.cancel_subscription(course_offering_id)
        if message == CANCEL_ACCEPTED:
            self.employee_service.cancel_subscription(course_offering_id)

        print(course_offering_id, message)
