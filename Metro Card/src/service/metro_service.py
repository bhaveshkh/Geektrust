from src.models.station import Station
from src.models.metro_card import MetroCard
from src.models.passenger import Passenger
from src.core.exceptions import (
    MetroCardExistsException,
    InvalidCardException,
    InvalidPassengerException,
    InvalidStationException,
)
from src.core.utils import get_service_charge
from src.core.constants import *


class MetroService:
    def __init__(self):
        self.stations = {}
        for station_name in AVAILABLE_STATIONS:
            self.stations[f"{station_name}"] = Station(f"{station_name}")

        self.passengers = {}
        for passenger_type, passenger_fare in PASSENGERS_TYPES.items():
            self.passengers[passenger_type] = Passenger(passenger_type, passenger_fare)
        self.metro_cards = {}

    def get_stations(self):
        return self.stations

    def add_card(self, card_id, balance):
        if card_id not in self.metro_cards:
            self.metro_cards[card_id] = MetroCard(card_id, balance, 0)
        else:
            raise MetroCardExistsException

    def process_journey(self, card_id, passenger_type, source_station):
        card = self.metro_cards.get(card_id)
        if not card:
            raise InvalidCardException

        if passenger_type not in self.passengers:
            raise InvalidPassengerException

        if source_station not in self.stations:
            raise InvalidStationException

        card.add_trip()

        is_discount_applicable = card.discount_applicable()
        journey_fare = 0
        service_charge = 0
        discount = 0
        passenger_fare = self.passengers[passenger_type].get_passenger_fare()
        if not is_discount_applicable:
            journey_fare = passenger_fare
        else:
            journey_fare = self.passengers[passenger_type].get_discounted_fare()
            discount = passenger_fare - journey_fare
            self.stations[source_station].add_discount(discount)

        metro_card_balance = card.get_balance()
        if journey_fare < metro_card_balance:
            self.metro_cards[card_id].deduct_balance(journey_fare)
            self.stations[source_station].add_collection(journey_fare)

        else:
            recharge_amount = journey_fare - metro_card_balance
            service_charge = get_service_charge(recharge_amount)
            self.stations[source_station].add_collection(journey_fare + service_charge)
            card.deduct_balance(metro_card_balance)

        self.stations[source_station].add_passenger_trip(passenger_type)

    def get_station_collections(self):
        stations_collections = {}

        for stations_name, stations_object in self.stations.items():
            stations_collections[stations_name] = self.stations[
                stations_name
            ].get_total_collection()
        return stations_collections

    def get_station_discounts(self):
        stations_discount = {}

        for stations_name, stations_object in self.stations.items():
            stations_discount[stations_name] = self.stations[
                stations_name
            ].get_total_discount()
        return stations_discount

    def get_station_visit_summary(self):
        station_visit_summary = {}

        for stations_name, stations_object in self.stations.items():
            station_visit_summary[
                stations_name
            ] = stations_object.get_passengers_summary()
        return station_visit_summary
