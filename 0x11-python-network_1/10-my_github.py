#!/usr/bin/python3
"""
Script that uses Basic Authentication with a personal access token
to access the GitHub API and display the user ID.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Usage: {} <username> <personal_access_token>".format(sys.argv[0]))

    username = sys.argv[1]
    token = sys.argv[2]

    # GitHub API endpoint for authenticated user details
    url = "https://api.github.com/user"

    # Set up Basic Authentication with username and personal access token
    auth = (username, token)

    # Send GET request to GitHub API with Basic Authentication
    response = requests.get(url, auth=auth)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        user_info = response.json()
        user_id = user_info.get('id')
        print(user_id)
    else:
        print("None")
