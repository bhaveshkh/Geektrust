from sys import argv

from src.service.command_processor import CommandProcessor


def main():
    if len(argv) != 2:
        raise Exception("Invalid input")

    command_processor = CommandProcessor()

    # Read input file
    input_file_path = argv[1]
    f = open(input_file_path, 'r')
    lines = f.readlines()

    for line in lines:
        line_args = line.strip().split()
        command = line_args[0].upper()
        args = line_args[1:]

        command_processor.process_command(command, *args)


if __name__ == "__main__":
    main()
