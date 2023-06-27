from sys import argv
from src.service.metro_service import MetroService
from src.service.print_service import PrintService
from src.core.exceptions import InvalidInputException


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

        if line_args[0].upper() == "BALANCE":
            command, card_id, balance = (
                line_args[0].upper(),
                line_args[1].upper(),
                int(line_args[2]),
            )
            metro_service.add_card(card_id, balance)

        elif line_args[0].upper() == "CHECK_IN":
            command, card_id, passenger_type, source_station = (
                line_args[0].upper(),
                line_args[1].upper(),
                line_args[2].upper(),
                line_args[3].upper(),
            )
            metro_service.process_jounrey(card_id, passenger_type, source_station)

        elif line_args[0].upper() == "PRINT_SUMMARY":
            pass

        else:
            print(line)
            raise InvalidInputException

    print_service.print_output(metro_service)


if __name__ == "__main__":
    main()
