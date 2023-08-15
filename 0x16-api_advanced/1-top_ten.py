#!/usr/bin/python3
""" Module for task 1"""


def top_ten(subreddit):
    """ Prints the titles of the first 10 hot posts
    listed for a given subreddit"""
    import requests

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "My Reddit API Client"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data.get("data", {}).get("children", [])

        if not posts:
            print("None")
            return
        for post in posts[:10]:
            title = post.get("data", {}).get("title")
            print(title)
        else:
            print("Invalid subreddit.")
