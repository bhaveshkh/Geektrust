from src.core.constants import AVAILABLE_STATIONS


class PrintService:
    def print_output(self, metro_service):
        total_collections = metro_service.get_station_collections()
        total_discounts = metro_service.get_station_discounts()
        station_visit_summary = metro_service.get_station_visit_summary()

        for station_name in AVAILABLE_STATIONS:
            print(
                f"TOTAL_COLLECTION    {station_name}   {total_collections[station_name]}   {total_discounts[station_name]}"
            )
            print("PASSENGER_TYPE_SUMMARY")
            for passenger_type, no_visits in station_visit_summary[
                station_name
            ].items():
                if no_visits:
                    print(f"{passenger_type} {no_visits}")
