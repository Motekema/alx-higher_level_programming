#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL,
and displays the value of the variable X-Request-Id in the response header.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    response = requests.get(url)
    
    # Check if X-Request-Id is present in the response headers
    if 'X-Request-Id' in response.headers:
        print(response.headers['X-Request-Id'])
    else:
        print("No X-Request-Id found in the response headers.")
