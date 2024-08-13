#!/usr/bin/python3
''' function that queries the Reddit API
and returns the number of subscribers '''

import requests


def number_of_subscribers(subreddit):
    ''' Args:
        subreddit name
    Returns:
        no of subs or 0 if failed '''
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
            'User-Agent': 'TamirALX:API_Task:v1.0 (by /u/coldshawerma)'}
    redd = requests.get(url, headers=headers, allow_redirects=False)
    if redd.status_code == 200:
        results = redd.json()
        return (results.get("data").get("subscribers"))
    else:
        return (0)
