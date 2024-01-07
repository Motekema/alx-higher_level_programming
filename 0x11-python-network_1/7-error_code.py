
#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL, and displays the body of the response.
If the HTTP status code is greater than or equal to 400, it prints: Error code: followed by the value of the HTTP status code.
"""

import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
