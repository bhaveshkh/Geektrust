import unittest
from src.models.station import Station
from src.core.constants import PASSENGERS_TYPES


class StationTestCase(unittest.TestCase):
    def setUp(self):
        self.station = Station("Central")

    def test_get_total_collection(self):
        self.assertEqual(self.station.get_total_collection(), 0)

    def test_get_passengers_summary(self):
        self.assertEqual(
            self.station.get_passengers_summary(),
            {passenger_type: 0 for passenger_type in PASSENGERS_TYPES},
        )


    def test_add_collection(self):
        initial_total_collection = self.station.get_total_collection()

        self.station.add_collection(100)
        self.assertEqual(
            self.station.get_total_collection(), initial_total_collection + 100
        )

    def test_add_discount(self):
        initial_total_discount = self.station.get_total_discount()

        self.station.add_discount(50)
        self.assertEqual(self.station.get_total_discount(), initial_total_discount + 50)

    def test_get_total_discount(self):
        self.assertEqual(self.station.get_total_discount(), 0)

    def test_to_string(self):
        expected_string = "Name: Central, Total_collection: 0, Passengers: {'ADULT': 0, 'SENIOR_CITIZEN': 0, 'KID': 0}"
        self.assertEqual(str(self.station), expected_string)


if __name__ == "__main__":
    unittest.main()
