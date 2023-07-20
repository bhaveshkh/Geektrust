from sys import argv
from src.service.metro_service import MetroService
from src.service.print_service import PrintService
from src.core.exceptions import InvalidInputException
from src.core.command_processor import BalanceCommandProcessor, CheckInCommandProcessor, PrintSummaryCommandProcessor

balance_processor = BalanceCommandProcessor()
check_in_processor = CheckInCommandProcessor()
print_summary_processor = PrintSummaryCommandProcessor()


def main():
    metro_service = MetroService()
    print_service = PrintService()

    if len(argv) != 2:
        raise Exception("File path not entered")

    file_path = argv[1]
    f = open(file_path, "r")
    lines = f.readlines()

    for line in lines:
        line_args = line.strip().split(" ")
        command = line_args[0].upper()

        if command == "BALANCE":
            card_id, balance = line_args[1].upper(), int(line_args[2])
            balance_processor.process(metro_service, card_id, balance)

        elif command == "CHECK_IN":
            card_id, passenger_type, source_station = line_args[1].upper(), line_args[2].upper(), line_args[3].upper(),
            check_in_processor.process(
                metro_service, card_id, passenger_type, source_station)

        elif command == "PRINT_SUMMARY":
            print_summary_processor.process(print_service, metro_service)

        else:
            print(line)
            raise InvalidInputException


if __name__ == "__main__":
    main()
