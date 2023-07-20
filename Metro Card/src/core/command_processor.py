class BalanceCommandProcessor:
    def process(self, metro_service, card_id, balance):
        metro_service.add_card(card_id, balance)


class CheckInCommandProcessor:
    def process(self, metro_service, card_id, passenger_type, source_station):
        metro_service.process_journey(card_id, passenger_type, source_station)


class PrintSummaryCommandProcessor:
    def process(self, print_service, metro_service):
        print_service.print_output(metro_service)
