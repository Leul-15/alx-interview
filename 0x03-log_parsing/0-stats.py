#!/usr/bin/python3
""" """
import sys
import signal
from collections import defaultdict

def signal_handler(sig, frame):
    """ Signal handler """
    print_statistics()
    sys.exit(0)

def print_statistics():
    """ Print statistics """
    global total_size, status_counts
    print("Total file size:", total_size)
    for status_code in sorted(status_counts.keys()):
        print(f"{status_code}: {status_counts[status_code]}")

total_size = 0
status_counts = defaultdict(int)
line_count = 0

signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) < 7 or parts[-2] not in ["200", "301", "400", "401",
                "403", "404", "405", "500"]:
            continue
        ip_address = parts[0]
        status_code = parts[-2]
        try:
            file_size = int(parts[-1])
        except ValueError:
            continue

        total_size += file_size
        status_counts[status_code] += 1
        line_count += 1

        if line_count % 10 == 0:
            print_statistics()

except KeyboardInterrupt:
    print_statistics()
    sys.exit(0)
