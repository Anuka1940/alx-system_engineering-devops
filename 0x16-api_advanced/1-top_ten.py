#!/usr/bin/python3
""" Module for task 1"""
import requests


def top_ten(subreddit):
    """ Prints the titles of the first 10 hot posts
    listed for a given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "My Reddit API Client"}
    response = requests.get(url, headers=headers)

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
