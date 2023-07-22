class Employee:
    def __init__(self, email, course_id):
        self.courses = {}
        self.email = email
        self.name = self.email.split('@')[0]
        # Set the course_id vs course_reg_id
        self.courses[course_id] = f"REG-COURSE-{self.name}-{course_id.split('-')[1]}"

    def get_course_offering_id(self, course_id):
        return self.courses.get(course_id)

    def get_email(self):
        return self.email
