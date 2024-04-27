#!/usr/bin/python3
'''script that takes 2 arguments and list 10 commits
(from the most recent to oldest) of the repository
first argument by the user second arg'''

import requests
import sys


if __name__ == "__main__":

    url = f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits"
    response = requests.get(url)
    content = response.json()[:10]
    for commit in content:
        commit_info = commit.get('commit')
        tree_info = commit_info.get('tree', {}).get('sha', 'Unknown')
        author_name = commit_info.get('author', {}).get('name', 'Unknown')
        print(f"{tree_info}: {author_name}")
