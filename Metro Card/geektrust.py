from sys import argv
from src.service.metro_service import MetroService
from src.service.print_service import PrintService
from src.core.exceptions import InvalidInputException

def main():
    metro_service = MetroService()
    print_service = PrintService()

    if len(argv) != 2:
        raise InvalidInputException("File path not entered")

    file_path = argv[1]
    process_input_file(file_path, metro_service, print_service)

def process_input_file(file_path, metro_service, print_service):
    with open(file_path, "r") as f:
        lines = f.readlines()

    for line in lines:
        process_command_line(line.strip(), metro_service, print_service)

def process_command_line(line, metro_service, print_service):
    line_args = line.split()
    command = line_args[0].upper()

    if command == "BALANCE":
        card_id, balance = line_args[1].upper(), int(line_args[2])
        metro_service.add_card(card_id, balance)

    elif command == "CHECK_IN":
        card_id, passenger_type, source_station = line_args[1].upper(), line_args[2].upper(), line_args[3].upper()
        metro_service.process_journey(card_id, passenger_type, source_station)

    elif command == "PRINT_SUMMARY":
        print_service.print_output(metro_service)

    else:
        print(line)
        raise InvalidInputException("Invalid command provided")

if __name__ == "__main__":
    main()