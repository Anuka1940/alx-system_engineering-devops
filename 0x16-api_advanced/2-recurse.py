#!/usr/bin/python3
""" Module for task 2"""


def recurse(subreddit, hot_list=[], count=0, after=None):
    """Queries the Reddit API and returns all hot posts
    of the subreddit"""
    import requests

    response = requests.get("https://www.reddit.com/r/{}/hot.json"
                            .format(subreddit),
                            params={"count": count, "after": after},
                            headers={"User-Agent": "My User Agent"},
                            allow_redirects=False)
    if response.status_code >= 400:
        return None

    hot_1 = hot_list + [child.get("data").get("title")
                        for child in response.json()
                        .get("data", {})
                        .get("children", {})]

    info = response.json()
    if not info.get("data").get("after"):
        return hot_1

    return recurse(subreddit, hot_1, info.get("data").get("count"),
                   info.get("data").get("after"))
