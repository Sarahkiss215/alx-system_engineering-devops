#!/usr/bin/python3
"""Qeries the Reddit API and returns the number of subscribers"""

import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    req = requests.get(url, headers={'User-Agent': 'Python/requests'})

    try:
        resp = req.json()
        return resp.get("data", {}).get("subscribers", 0)
    except Exception:
        return 0
