#!/usr/bin/python3
"""Log parsing script that computes metrics from web server logs."""

import sys


def print_stats(total_size, status_codes):
    """Print statistics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        if status_codes[code] != 0:
            print("{}: {}".format(code, status_codes[code]))


def process_logs():
    """Process log lines from stdin."""
    total_size = 0
    status_codes = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
    }

    count = 0

    try:
        for line in sys.stdin:
            parts = line.split()

            if len(parts) < 2:
                continue

            try:
                status = int(parts[-2])
                size = int(parts[-1])
            except ValueError:
                continue

            total_size += size

            if status in status_codes:
                status_codes[status] += 1

            count += 1

            if count == 10:
                print_stats(total_size, status_codes)
                count = 0

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        return

    print_stats(total_size, status_codes)


if __name__ == "__main__":
    process_logs()
