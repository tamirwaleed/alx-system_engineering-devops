#!/usr/bin/python3
"""prints the titles of the first 10 hot posts
listed for a given subreddit"""

import requests


def top_ten(subreddit):
    """ Returns top 10 hottest posts"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
            'User-Agent': 'linux:tamir.alx:v1.0.0 (by /u/coldshawerma)'}
    params = {'limit': 10}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        results = response.json()
        for x in results["data"]["children"]:
            print(x.get("data").get("title"))
    else:
        print(None)
