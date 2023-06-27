class InvalidInputException(Exception):
    def __init__(self, message="Invalid input provided."):
        self.message = message
        super().__init__(self.message)


class MetroCardExistsException(Exception):
    def __init__(self, message="Metro Card already exists."):
        self.message = message
        super().__init__(self.message)


class InvalidCardException(Exception):
    def __init__(self, message="Metro card doesn't exist."):
        self.message = message
        super().__init__(self.message)


class InvalidPassengerException(Exception):
    def __init__(self, message="Passenger type doesn't exist."):
        self.message = message
        super().__init__(self.message)


class InvalidStationException(Exception):
    def __init__(self, message="Station doesn't exist."):
        self.message = message
        super().__init__(self.message)
