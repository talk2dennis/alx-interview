#!/usr/bin/python3
""" Log parsing module """
import sys


import sys
import signal
import re

# Initialize counters and storage for metrics
total_size = 0
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
line_count = 0

# Regular expression for matching the log format
log_pattern = re.compile(r'^\S+ - \[\S+ \S+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$')

def print_statistics():
    """Print the collected statistics."""
    global total_size, status_counts
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")

def handle_sigint(signum, frame):
    """Handle the SIGINT signal (Ctrl + C) and print statistics."""
    print("\nCaught SIGINT (Ctrl + C), printing statistics...")
    print_statistics()
    sys.exit(0)

# Register the SIGINT signal handler
signal.signal(signal.SIGINT, handle_sigint)

print("Reading from stdin. Press Ctrl+C to exit.")

try:
    for line in sys.stdin:
        match = log_pattern.match(line.strip())
        if match:
            status_code = int(match.group(1))
            file_size = int(match.group(2))

            total_size += file_size
            if status_code in status_counts:
                status_counts[status_code] += 1

            line_count += 1

            if line_count % 10 == 0:
                print_statistics()
                print()  # Print a blank line for readability

except KeyboardInterrupt:
    print("\nKeyboard interrupt received while reading from stdin.")
    print_statistics()
    sys.exit(0)

# Print final statistics after reading all lines
print_statistics()
