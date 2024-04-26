#!/usr/bin/python3
'''script that fetches https://alx-intranet.hbtn.io/status'''

import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    content = response
    print('Body response:')
    print('\t- type:', type(content.text))
    print('\t- content:', content.text)
