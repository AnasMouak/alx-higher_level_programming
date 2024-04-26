#!/usr/bin/python3
'''script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.'''

import requests
import sys

if __name__ == "__main__":
    
    if (len(sys.argv) == 1):
        arg = ""
    else:
        arg = sys.argv[1]

    data = {'q': arg}
    response = requests.post('http://0.0.0.0:5000/search_user', data=data)
    content = response.json()
    if content:
        print(f"{[content.get('id')]} {content.get('name')}")
    else:
        print('No result')
