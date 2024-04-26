#!/usr/bin/python3
'''script that takes in a URL and an email, sends a POST request to the URL
with the email as a parameter, and displays the body of the response'''

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":

    data = urllib.parse.urlencode({'email': sys.argv[2]}).encode('utf-8')
    req = urllib.request.Request(sys.argv[1], data=data, method='POST')
    with urllib.request.urlopen(req) as response:
        content = response.read().decode('utf-8')
        print(content)
