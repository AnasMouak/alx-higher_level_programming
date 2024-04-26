#!/usr/bin/python3
'''script that takes in a URL, sends a request to the URL and displays
    the body of the response'''

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":

    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            content = response.read().decode('utf-8')
            print(content)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
