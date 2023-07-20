from src.core.constants import PASSENGERS_TYPES


class Station:
    name = None
    total_collection = None
    passengers = {}

    def __init__(self, name=None):
        self.name = name
        self.total_collection = 0
        self.total_discount = 0

        self.passengers = {}
        for passenger_type in PASSENGERS_TYPES:
            self.passengers[passenger_type] = 0

    def get_total_collection(self):
        return self.total_collection

    def get_passengers_summary(self):
        passenger_counts = self.passengers

        # Check if all values in the dictionary are the same
        if len(set(passenger_counts.values())) == 1:

            return dict(sorted(passenger_counts.items()))

        sorted_passenger_counts = {
            passenger_type: count
            for passenger_type, count in sorted(
                passenger_counts.items(), key=lambda item: item[1], reverse=True
            )
        }

        top_two_passenger_types = list(sorted_passenger_counts.keys())[:2]
        passenger_type_with_lowest_count = min(
            sorted_passenger_counts, key=sorted_passenger_counts.get
        )

        summary_dict = {
            passenger_type: sorted_passenger_counts[passenger_type]
            for passenger_type in top_two_passenger_types
        }
        summary_dict[passenger_type_with_lowest_count] = sorted_passenger_counts[
            passenger_type_with_lowest_count
        ]

        return summary_dict

    def add_passenger_trip(self, passenger_type):
        self.passengers[passenger_type] += 1

    def add_collection(self, amount):
        self.total_collection += amount

    def add_discount(self, amount):
        self.total_discount += amount

    def get_total_discount(self):
        return self.total_discount

    def __str__(self):
        return f"Name: {self.name}, Total_collection: {self.total_collection}, Passengers: {self.passengers}"
