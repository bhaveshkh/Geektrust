import unittest
from src.models.metro_card import MetroCard

class MetroCardTestCase(unittest.TestCase):
    def setUp(self):
        self.metro_card = MetroCard("MC1", 500, 3)

    def test_get_balance(self):
        self.assertEqual(self.metro_card.get_balance(), 500)

    def test_get_id(self):
        self.assertEqual(self.metro_card.get_id(), "MC1")

    def test_get_trips(self):
        self.assertEqual(self.metro_card.get_trips(), 3)

    def test_discount_applicable(self):
        self.assertFalse(self.metro_card.discount_applicable())

        self.metro_card.add_trip()
        self.assertTrue(self.metro_card.discount_applicable())

    def test_add_trip(self):
        initial_trips = self.metro_card.get_trips()
        self.metro_card.add_trip()
        self.assertEqual(self.metro_card.get_trips(), initial_trips + 1)

    def test_add_balance(self):
        initial_balance = self.metro_card.get_balance()
        self.metro_card.add_balance(100)
        self.assertEqual(self.metro_card.get_balance(), initial_balance + 100)

    def test_deduct_balance(self):
        initial_balance = self.metro_card.get_balance()
        self.metro_card.deduct_balance(50)
        self.assertEqual(self.metro_card.get_balance(), initial_balance - 50)

    def test_to_string(self):
        expected_string = "id: MC1 balance: 500 trips: 3"
        self.assertEqual(str(self.metro_card), expected_string)

if __name__ == '__main__':
    unittest.main()
