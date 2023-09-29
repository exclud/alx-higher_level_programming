#!/usr/bin/python3
"""
This script uses Basic Authentication with a personal
access token to access the GitHub API
and displays the user ID of the authenticated user.
"""

import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    personal_access_token = sys.argv[2]
    headers = {
        "Authorization": f"token {personal_access_token}"
    }

    try:
        # Send a GET request to retrieve user information
        response = requests.get("https://api.github.com/user", headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            user_info = response.json()
            user_id = user_info.get("id")
            print(user_id)
        else:
            print(f"Error: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
