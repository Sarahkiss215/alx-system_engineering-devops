#!/usr/bin/python3
"""Queries the Reddit API and returns list with titles all hot articles"""


import requests


def recurse(subreddit, hot_list=[], after=None):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {
        "after": after
    }
    req = requests.get(
        url, headers={'User-Agent': 'Python/requests'}, params=params)
    try:
        resp = req.json()
        posts = resp.get("data", {}).get("children", None)
        after = resp.get("data", {}).get("after", None)
        if posts is not None:
            [hot_list.append(post.get("data").get("title")) for post in posts]
        if after is None:
            if len(hot_list) == 0:
                return None
            return hot_list
        else:
            return recurse(subreddit, hot_list, after=after)
    except Exception:
        return None
