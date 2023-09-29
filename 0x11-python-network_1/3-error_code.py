#!/usr/bin/python3
"""
This script sends a request to a URL and displays
the body of the response (decoded in utf-8).
It handles HTTP errors and prints the error code in case of an error.
"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            content = response.read().decode('utf-8')
            print(content)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
