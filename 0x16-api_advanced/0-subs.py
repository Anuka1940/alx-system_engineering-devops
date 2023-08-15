#!/usr/bin/python3
""" Module for task 0 """


import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    to the subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "My Reddit API Client"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()["data"]["subscribers"]
    else:
        return 0
