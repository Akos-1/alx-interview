#!/usr/bin/python3

import sys


def print_message(dict_status_code, total_file_size):
    """
    Data to be printed
    Args:
        dict_status_code: dictionary of status codes
        total_file_size: the total file
    Returns:
        nothing
    """
    print("File size: {}".format(total_file_size))
    for key, val in sorted(dict_status_code.items()):
        if val != 0:
            print("{}: {}".format(key, val))


total_file_size = 0
line_count = 0
status_codes = {"200": 0,
                "301": 0,
                "400": 0,
                "401": 0,
                "403": 0,
                "404": 0,
                "405": 0,
                "500": 0}

try:
    for line in sys.stdin:
        parsed_line = line.split()
        parsed_line = parsed_line[::-1]

        if len(parsed_line) > 2:
            line_count += 1

            if line_count <= 10:
                total_file_size += int(parsed_line[0])
                code = parsed_line[1]

                if code in status_codes:
                    status_codes[code] += 1
                if line_count == 10:
                    print_message(status_codes, total_file_size)
                    line_count = 0

finally:
    print_message(status_codes, total_file_size)
