#!/usr/bin/python3
"""
Script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    # Send a POST request to the URL with the letter as a parameter
    response = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})

    try:
        # Parse the JSON response
        json_response = response.json()

        # Check if the JSON is not empty
        if json_response:
            print("[{}] {}".format(json_response['id'], json_response['name']))
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")
