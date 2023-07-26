import unittest
from src.core.exception import CourseExistsException
from src.core.utils import format_date
from src.models.course import Course
from src.service.course_service import CourseService
from collections import defaultdict

class TestCourseService(unittest.TestCase):
    def setUp(self):
        self.course_service = CourseService()

    def test_add_course_offering(self):
        course_id = self.course_service.add_course_offering("PYTHON", "JOHN", "08012023", 5, 20)
        self.assertIsNotNone(course_id)
        self.assertTrue(self.course_service.is_valid_course_id(course_id))

        with self.assertRaises(CourseExistsException):
            self.course_service.add_course_offering("PYTHON", "JOHN", "09012023", 8, 25)

    def test_get_course_details(self):
        course_id = self.course_service.add_course_offering("DATASCIENCE", "JANE", "01102023", 10, 30)
        course_details = self.course_service.get_course_details(course_id)

        self.assertEqual(course_details['course_name'], "DATASCIENCE")
        self.assertEqual(course_details['instructor_name'], "JANE")
        self.assertEqual(course_details['start_data'], "01-10-2023")
        self.assertEqual(course_details['course_offering_ids'], None)

    def test_perform_course_allotment(self):
        course_id = self.course_service.add_course_offering("DATASCIENCE", "JANE", "01102023", 10, 30)
        status = self.course_service.perform_course_allotment(course_id)
        self.assertFalse(status)

        self.course_service.add_employee_to_course(course_id, "OFFERING-001")
        status = self.course_service.perform_course_allotment(course_id)
        self.assertFalse(status)

    def test_is_valid_course_id(self):
        course_id = self.course_service.add_course_offering("DATASCIENCE", "JANE", "01102023", 10, 30)
        self.assertTrue(self.course_service.is_valid_course_id(course_id))
        self.assertFalse(self.course_service.is_valid_course_id("INVALID_COURSE_ID"))

    def test_is_course_available(self):
        course_id = self.course_service.add_course_offering("DATASCIENCE", "JANE", "01102023", 10, 30)
        self.assertTrue(self.course_service.is_course_available(course_id))

        for _ in range(30):
            self.course_service.add_employee_to_course(course_id, f"OFFERING-{_}")

        self.assertFalse(self.course_service.is_course_available(course_id))

    def test_add_employee_to_course(self):
        course_id = self.course_service.add_course_offering("DATASCIENCE", "JANE", "01102023", 10, 30)

        for i in range(10):
            self.course_service.add_employee_to_course(course_id, f"OFFERING-{i}")

        course = self.course_service.courses[course_id]
        self.assertEqual(course.registered_employees, 10)
        self.assertEqual(len(self.course_service.course_participants[course_id]), 10)

    def test_cancel_subscription(self):
        course_id = self.course_service.add_course_offering("DATASCIENCE", "JANE", "01102023", 0, 30)
        self.course_service.add_employee_to_course(course_id, "OFFERING-001")

        # Try canceling a subscription before course allotment
        course_offering_id = "OFFERING-001"
        result, status = self.course_service.cancel_subscription(course_offering_id)
        self.assertEqual(result, "OFFERING-001")
        self.assertEqual(status, "CANCEL_ACCEPTED")

        # Perform course allotment
        self.course_service.add_employee_to_course(course_id, "OFFERING-001")
        self.course_service.perform_course_allotment(course_id)

        # Try canceling a subscription after course allotment
        result, status = self.course_service.cancel_subscription(course_offering_id)
        self.assertEqual(result, "OFFERING-001")
        self.assertEqual(status, "CANCEL_REJECTED")

if __name__ == "__main__":
    unittest.main()
