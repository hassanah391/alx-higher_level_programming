#!/usr/bin/python3
"""
A script that uses Github API to list last 10 commits
"""
import requests
from sys import argv

if __name__ == "__main__":

    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        argv[2], argv[1])
    r = requests.get(url)
    list_commits = r.json()

    for commit in list_commits[0:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
