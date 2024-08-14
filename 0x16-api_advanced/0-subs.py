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
            "User-Agent":
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        results = response.json()
        return (results.get("data").get("subscribers"))
    else:
        return (0)
