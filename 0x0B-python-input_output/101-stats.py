#!/usr/bin/python3
"""Script to read stdin line by line"""
import sys
import signal

# Define a dictionary to store the statistics
statistics = {
    'total_size': 0,
    'status_codes': {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0
    }
}

# Define a counter to keep track of the number of lines read
line_count = 0

# Define a signal handler for keyboard interruption (CTRL + C)
def signal_handler(signal, frame):
    """
    Signal handler for keyboard interruption (CTRL + C).
    Prints the current statistics and exits the program.
    """
    print_statistics()
    sys.exit(0)

# Define a function to print the statistics
def print_statistics():
    """
    Prints the current statistics including the total file size and the number of lines by status code.
    """
    print(f"Total file size: {statistics['total_size']}")

    for code, count in sorted(statistics['status_codes'].items()):
        if count > 0:
            print(f"{code}: {count}")

# Register the signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

try:
    # Read stdin line by line
    for line in sys.stdin:
        # Split the line by space to extract the status code and file size
        parts = line.split(' ')
        status_code = parts[8]
        file_size = parts[8]

        # Update the total file size
        statistics['total_size'] += int(file_size)

        # Update the count for the status code
        if status_code in statistics['status_codes']:
            statistics['status_codes'][status_code] += 1

        # Increment the line count
        line_count += 1

        # Print the statistics every 10 lines
        if line_count % 10 == 0:
            print_statistics()

except KeyboardInterrupt:
    # Handle keyboard interruption (CTRL + C)
    print_statistics()
    sys.exit(0)
