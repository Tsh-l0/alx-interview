#!/usr/bin/python3
"""
A log parsing script that reads stdin line by line
and computes the resulting metrics
"""
import sys
import re
import signal


def print_stats(total_size, status_counts):
    """
    Print the accummulated statistics
    """
    print(f"File size: {total_size}")
    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")


def main():
    """
    Main function to process log lines and compute metrics
    """
    total_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0,
                     403: 0, 404: 0, 405: 0, 500: 0}

    line_count = 0

    def signal_handler(sig, frame):
        """
        Handle keyboard termination of script
        """
        print_stats(total_size, status_counts)
        sys.exit(0)

    # Set up signal handler for ctrl c
    signal.signal(signal.SIGINT, signal_handler)

    try:
        for line in sys.stdin:
            # Parse the line using regex
            pattern = (r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \['
                       r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+\] '
                       r'"GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$')
            match = re.match(pattern, line.strip())

            if match:
                status_code = int(match.group(1))
                file_size = int(match.group(2))

                # Update metrics
                total_size += file_size
                if status_code in status_counts:
                    status_counts[status_code] += 1
                line_count += 1

                # Print stats every 10 lines
                if line_count % 10 == 0:
                    print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        raise


if __name__ == "__main__":
    main()
