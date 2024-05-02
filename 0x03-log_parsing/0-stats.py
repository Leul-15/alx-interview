#!/usr/bin/python3
import sys
import signal
from collections import defaultdict

def handler(sig, frame):
    """  Signal handler """
    print_stats()
    sys.exit(0)

def print_stats():
    """ Print statistics """
    global size, status_counts
    print("Total file size:", size)
    for status_code in sorted(status_counts.keys()):
        print(f"{status_code}: {status_counts[status_code]}")

size = 0
status_counts = defaultdict(int)
line_count = 0

signal.signal(signal.SIGINT, handler)

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) < 7:
            continue
        ip_address = parts[0]
        status_code = parts[-2]
        file_size = int(parts[-1])

        size += file_size
        status_counts[status_code] += 1
        line_count += 1

        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)
