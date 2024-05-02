#!/usr/bin/python3
"""Parsing logs
"""
import sys
from collections import defaultdict

status_codes = defaultdict(int)
file_size = 0


def print_stats(file_size, status_codes):
    """
    """
    print("File size: {}".format(file_size))
    for status_code, count in sorted(status_codes.items()):
        if count:
            print("{}: {}".format(status_code, count))


def main():
    """
    """
    global status_codes, file_size
    line_count = 0

    for line in sys.stdin:
        line_count += 1
        data = line.split()
        try:
            file_size += int(data[-1])
            status_codes[int(data[-2])] += 1
        except (ValueError, IndexError):
            pass

        if line_count % 10 == 0:
            print_stats(file_size, status_codes)
    print_stats(file_size, status_codes)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print_stats(file_size, status_codes)
        raise
