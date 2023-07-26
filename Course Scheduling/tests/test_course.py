import unittest
from src.models.course import Course

class TestCourse(unittest.TestCase):
    def setUp(self):
        self.course = Course("PYTHON", "JOHN", "01082023", 5, 20)

    def test_course_properties(self):
        self.assertEqual(self.course.get_course_name(), "PYTHON")
        self.assertEqual(self.course.get_instructor_name(), "JOHN")
        self.assertEqual(self.course.get_start_date(), "01082023")
        self.assertEqual(self.course.min_employees, 5)
        self.assertEqual(self.course.max_employees, 20)
        self.assertEqual(self.course.allotted, False)
        self.assertEqual(self.course.registered_employees, 0)
        self.assertEqual(self.course.get_course_id(), "OFFERING-PYTHON-JOHN")

    def test_course_allotment_status(self):
        self.assertEqual(self.course.get_course_allotment_status(), False)
        self.course.registered_employees = 10
        self.assertEqual(self.course.set_course_allotment_status(), True)
        self.assertEqual(self.course.get_course_allotment_status(), True)
        self.course.registered_employees = 3
        self.assertEqual(self.course.set_course_allotment_status(), False)
        self.assertEqual(self.course.get_course_allotment_status(), False)

    def test_is_course_available(self):
        self.assertEqual(self.course.is_course_available(), True)
        self.course.registered_employees = 15
        self.assertEqual(self.course.is_course_available(), True)

    def test_increase_registered_employees(self):
        self.assertEqual(self.course.registered_employees, 0)
        self.course.increase_registered_employees()
        self.assertEqual(self.course.registered_employees, 1)
        self.course.increase_registered_employees()
        self.assertEqual(self.course.registered_employees, 2)

if __name__ == "__main__":
    unittest.main()
