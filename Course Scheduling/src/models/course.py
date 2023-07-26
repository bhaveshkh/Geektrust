class Course:
    def __init__(self, name, instructor_name, start_date, min_employees, max_employees):
        self.course_name = name
        self.instructor_name = instructor_name
        self.min_employees = min_employees
        self.max_employees = max_employees
        self.start_date = start_date
        self.course_id = f"OFFERING-{self.course_name}-{self.instructor_name}"
        self.allotted = False
        self.registered_employees = 0

    def get_course_id(self):
        return self.course_id

    def __str__(self):
        return f"course_name: {self.course_name}  instructor_name: {self.instructor_name}  " \
               f"start_date: {self.start_date}  min_employees: {self.min_employees}  max_employees: {self.max_employees}  " \
               f"allotted: {self.allotted}  course_id: {self.course_id}  registered_emps : {self.registered_employees}"

    def get_course_allotment_status(self):
        return self.allotted

    def is_course_available(self):
        if not self.allotted and self.registered_employees < self.max_employees:
            return True
        else:
            return False

    def set_course_allotment_status(self):
        if self.registered_employees > self.min_employees:
            self.allotted = True
            return True
        else:
            self.allotted = False
            return False

    def get_course_name(self):
        return self.course_name

    def get_instructor_name(self):
        return self.instructor_name

    def get_start_date(self):
        return self.start_date

    def increase_registered_employees(self):
        self.registered_employees += 1