import unittest
from src.models.employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee("JOHN@example.com", "OFFERING-PYTHON-JOHN")

    def test_employee_properties(self):
        self.assertEqual(self.employee.email, "JOHN@example.com")
        self.assertEqual(self.employee.name, "JOHN")
        self.assertEqual(self.employee.courses, {
            "OFFERING-PYTHON-JOHN": "REG-COURSE-JOHN-PYTHON"
        })

    def test_get_course_offering_id(self):
        course_id = "OFFERING-PYTHON-JOHN"
        expected_course_reg_id = "REG-COURSE-JOHN-PYTHON"
        self.assertEqual(self.employee.get_course_offering_id(course_id), expected_course_reg_id)

        course_id = "OFFERING-DATA-JANE"
        self.assertIsNone(self.employee.get_course_offering_id(course_id))

    def test_get_email(self):
        self.assertEqual(self.employee.get_email(), "JOHN@example.com")

if __name__ == "__main__":
    unittest.main()
