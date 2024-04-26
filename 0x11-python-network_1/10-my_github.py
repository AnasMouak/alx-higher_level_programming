#!/usr/bin/python3
'''script that takes your GitHub credentials (username and password)
    and uses the GitHub API to display your id'''

import requests
import sys

if __name__ == "__main__":

    auth = (sys.argv[1], sys.argv[2])
    response = requests.get('https://api.github.com/user', auth=auth)
    print(response.json().get('id'))
