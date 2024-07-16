#!/usr/bin/python3
"""
This module reads from standard input and computes metrics from the input.
"""

import sys


def print_stats(file_size, status_codes):
    """
    Print the file size and status codes.
    """
    print("File size: {}".format(file_size))
    for key, value in sorted(status_codes.items()):
        if value != 0:
            print("{}: {}".format(key, value))


def main():
    """
    Read from standard input and compute metrics.
    """
    file_size = 0
    status_codes = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
    }
    try:
        for i, line in enumerate(sys.stdin, 1):
            split_line = line.split()
            if len(split_line) < 2:
                continue
            file_size += int(split_line[-1])
            status_code = split_line[-2]
            if status_code in status_codes:
                status_codes[status_code] += 1
            if i % 10 == 0:
                print_stats(file_size, status_codes)
    except KeyboardInterrupt:
        print_stats(file_size, status_codes)
        raise


if __name__ == "__main__":
    main()
