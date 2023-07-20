class Passenger:
    def __init__(self, _type, fare=0):
        self.type = _type
        self.fare = fare
        self.discounted_fare = fare // 2

    def get_passenger_fare(self):
        return self.fare

    def get_discounted_fare(self):
        return self.discounted_fare

    def __str__(self):
        return f"type: {self.type} fare: {self.fare}"
