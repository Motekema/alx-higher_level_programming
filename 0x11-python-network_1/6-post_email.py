#!/usr/bin/python3
"""
Script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} <URL> <email>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]
    
    # Data to be sent in the POST request
    data = {'email': email}
    
    # Send POST request to the URL with email as a parameter
    response = requests.post(url, data=data)
    
    # Display the body of the response
    print("Your email is:", response.text)
