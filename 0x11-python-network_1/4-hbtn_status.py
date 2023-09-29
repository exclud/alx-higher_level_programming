#!/usr/bin/python3
"""
This script fetches the status from
https://alx-intranet.hbtn.io/status using the requests library
and displays the body of the response with formatting.
"""

import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    content = response.text

    print("Body response:")
    print(f"\t- type: {type(response.text).__name__}")
    print(f"\t- content: {response.text}")
