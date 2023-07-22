from src.models.employee import Employee


class EmployeeService:
    def __init__(self):
        self.employees = {}

    def register_employee(self, email, course_id):
        employee = Employee(email, course_id)
        course_offering_id = employee.get_course_offering_id(course_id)
        self.employees[course_offering_id] = employee
        return course_offering_id

    def get_employee_details(self, course_offering_id):
        employee = self.employees[course_offering_id]

        return employee.get_email()

    def cancel_subscription(self, course_offering_id):
        if course_offering_id in self.employees:
            self.employees.pop(course_offering_id)
