
#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL, and displays the body of the response.
If the HTTP status code is greater than or equal to 400, it prints: Error code: followed by the value of the HTTP status code.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]

    # Send a GET request to the URL
    response = requests.get(url)

    # Display the body of the response
    print(response.text)

    # Check if the HTTP status code is greater than or equal to 400
    if response.status_code >= 400:
        print("Error code:", response.status_code)
