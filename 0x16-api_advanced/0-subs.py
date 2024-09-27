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
            "User-Agent": 'TamirRedditApp/1.0 (by /u/coldshawerma)'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return (response.json().get("data").get("subscribers"))
    return (0)
