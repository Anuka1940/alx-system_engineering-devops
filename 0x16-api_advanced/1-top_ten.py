#!/usr/bin/python3
"""This module uses the reddit api to fetch data"""

import requests


def top_ten(subreddit):
    """Fetch top 10 posts using reddit api"""
    posts = requests.get(
        "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit),
        headers={"User-Agent": "My-User-Agent"},
        allow_redirects=False
    )
    if posts.status_code >= 300:
        print("None")
    else:
        children = posts.json().get('data').get('children')
        [print(child.get('data').get('title'))
            for child in children]
