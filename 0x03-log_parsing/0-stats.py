#!/usr/bin/python3

import sys


def print_message(dict_status_code, total_file_size):
    """
    Print statistics
    Args:
        dict_status_code: dictionary of status codes
        total_file_size: the total file size
    Returns:
        None
    """
    print("Total file size: {}".format(total_file_size))
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
        parts = line.split()
        if len(parts) == 7:
            line_count += 1
            total_file_size += int(parts[-1])
            status_code = parts[-2]
            if status_code in status_codes:
                status_codes[status_code] += 1
            if line_count % 10 == 0:
                print_message(status_codes, total_file_size)
                line_count = 0

except KeyboardInterrupt:
    print("\nKeyboard interrupt detected. Printing statistics:")
    print_message(status_codes, total_file_size)
    sys.exit(0)

print("\nEnd of file. Printing final statistics:")
print_message(status_codes, total_file_size)
