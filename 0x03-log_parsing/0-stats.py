#!/usr/bin/python3
"""A module for parsing logs.
"""
import sys
from collections import defaultdict

status_codes = defaultdict(int)
file_size = 0


def print_stats(file_size, status_codes):
    """Prints statistics about Nginx logs.

    This function takes the total file size and a dictionary of status code
    counts as arguments and prints the statistics. The function prints the
    total file size, followed by the number of lines for each status code.

    Args:
        file_size (int): The total file size.
        status_codes (dict): A dictionary of status code counts.

    Returns:
        None
    """
    print("File size: {}".format(file_size))
    for status_code, count in sorted(status_codes.items()):
        if count:
            print("{}: {}".format(status_code, count))


def main():
    """Reads Nginx logs from standard input and computes metrics.

    This function reads from standard input line by line, computes metrics,
    and prints statistics after every 10 lines or upon receiving a keyboard
    interrupt (CTRL + C). The function updates the global variables
    'file_size' and 'status_codes' to keep track of the total file size and
    status code counts.

    Returns:
        None
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
