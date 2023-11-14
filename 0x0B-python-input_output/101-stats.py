#!/usr/bin/python3
"""Reads from standard input and computes metrics. Prints statistics every 10 lines or on keyboard interruption (CTRL + C)."""

def print_stats(size, status_codes):
    """Print accumulated metrics.

    Args:
        size (int): Accumulated file size.
        status_codes (dict): Accumulated status code counts.
    """
    print(f"File size: {size}")
    for key in sorted(status_codes):
        print(f"{key}: {status_codes[key]}")

if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    valid_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_stats(size, status_codes)
                count = 1
            else:
                count += 1

            parts = line.split()
            
            try:
                size += int(parts[-1])
            except (IndexError, ValueError):
                pass

            try:
                code = parts[-2]
                if code in valid_codes:
                    status_codes[code] = status_codes.get(code, 0) + 1
            except IndexError:
                pass

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise

