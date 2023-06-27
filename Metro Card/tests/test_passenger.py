import unittest
from src.models.passenger import Passenger


class PassengerTestCase(unittest.TestCase):
    def setUp(self):
        self.passenger = Passenger("ADULT", 200)

    def test_get_passenger_fare(self):
        self.assertEqual(self.passenger.get_passenger_fare(), 200)

    def test_get_discounted_fare(self):
        self.assertEqual(self.passenger.get_discounted_fare(), 100)

    def test_to_string(self):
        self.assertEqual(str(self.passenger), "type: ADULT fare: 200")
