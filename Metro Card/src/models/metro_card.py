class MetroCard:
    def __init__(self, _id, balance, trips=0):
        self._id = _id
        self.balance = balance
        self.trips = trips

    def get_balance(self):
        return self.balance

    def get_id(self):
        return self._id

    def get_trips(self):
        return self.trips

    def discount_applicable(self):
        return self.trips % 2 == 0 and self.trips != 0

    def add_trip(self):
        self.trips += 1

    def add_balance(self, amount):
        self.balance += amount

    def deduct_balance(self, amount):
        self.balance -= amount

    def __str__(self):
        return f"id: {self._id} balance: {self.balance} trips: {self.trips}"
