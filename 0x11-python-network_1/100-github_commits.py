#!/usr/bin/python3
"""
This script uses the GitHub API to list the
10 most recent commits
from a specified repository by a given owner.
"""

import requests
import sys

if __name__ == "__main__":
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]

    # Create the GitHub API endpoint URL
    url = f"https://api.github.com/repos/{owner_name}/{repository_name}/commits"

    try:
        # Send a GET request to retrieve the commits
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            commits = response.json()

            # Print the 10 most recent commits
            for commit in commits[:10]:
                sha = commit.get("sha")
                author_name = commit.get("commit").get("author").get("name")
                print(f"{sha}: {author_name}")
        else:
            print(f"Error: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
