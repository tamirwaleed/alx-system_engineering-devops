#!/usr/bin/python3
''' function that queries the Reddit API
and returns the number of subscribers '''


import json
import requests
import sys


def number_of_subscribers(subreddit):
    ''' the function '''
    url = 'https://www.reddit.com/r/{}/about/.json'.format(subreddit)
    headers = {'User-Agent': 'MyRedditApp/0.0.1'}
    redd = requests.get(url, headers=headers, allow_redirects=False)
    if redd.status_code == 200:
        results = redd.json()
        return (results.get("data").get("subscribers"))
    else:
        return (0)
