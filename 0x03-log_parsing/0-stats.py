#!/usr/bin/python3

import sys

STATUS_CODES = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
total_file_size = 0
line_count = 0


def print_statistics():
    global total_file_size
    print(f"Total file size: {total_file_size}")
    for code, count in sorted(STATUS_CODES.items()):
        if count > 0:
            print(f"{code}: {count}")
    print()


def handle_interrupt():
    print("\nKeyboard interrupt detected. Printing statistics:")
    print_statistics()
    sys.exit(0)


try:
    for line in sys.stdin:
        parts = line.strip().split()
        if len(parts) != 7:
            continue
        try:
            status_code = int(parts[3])
            file_size = int(parts[6])
            if status_code in STATUS_CODES:
                STATUS_CODES[status_code] += 1
                total_file_size += file_size
                line_count += 1
        except ValueError:
            continue

        if line_count % 10 == 0:
            print_statistics()
except KeyboardInterrupt:
    handle_interrupt()
