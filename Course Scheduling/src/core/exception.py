class CourseExistsException(Exception):
    def __init__(self, message="Course with name exists"):
        self.message = message
        super().__init__(self.message)


class InvalidInputException(Exception):
    def __init__(self, message="INPUT_DATA_ERROR"):
        self.message = message
        super().__init__(self.message)


class InvalidCourseIdException(Exception):
    def __init__(self, message="Invalid course_id exception"):
        self.message = message
        super().__init__(self.message)