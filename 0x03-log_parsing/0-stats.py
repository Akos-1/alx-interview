#!/usr/bin/python3

import sys
import signal

# Dictionary to store status code counts
status_counts = {
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
    global total_file_size, line_count
    print(f"Total file size: {total_file_size}")
    for status_code, count in sorted(status_counts.items()):
        if count > 0:
            print(f"{status_code}: {count}")
    print()


def handle_interrupt(sig, frame):
    print("\nKeyboard interrupt detected. Printing statistics:")
    print_statistics()
    sys.exit(0)


# Register the signal handler for SIGINT (Ctrl+C)
signal.signal(signal.SIGINT, handle_interrupt)

for line in sys.stdin:
    line = line.strip()
    parts = line.split()
    if len(parts) != 7:
        continue
    try:
        status_code = int(parts[3])
        file_size = int(parts[6])
    except ValueError:
        continue

    total_file_size += file_size
    status_counts[status_code] += 1
    line_count += 1

    if line_count % 10 == 0:
        print_statistics()
