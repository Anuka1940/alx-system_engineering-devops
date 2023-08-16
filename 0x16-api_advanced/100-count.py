#!/usr/bin/python3
""" coount """


def count_words(subreddit, word_list, after=None, counts=None):
    """ A recursive function that queries the Reddit API, parses the titles
    of all hot articles, and prints a sorted count of given keywords"""
    import requests

    if counts is None:
        counts = {}

    sub_info = requests.get("https://www.reddit.com/r/{}/hot.json"
                            .format(subreddit),
                            params={"after": after},
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)

    if sub_info.status_code >= 400:
        return

    titles = [post.get("data").get("title") for post in sub_info.json()
              .get("data")
              .get("children")]

    for title in titles:
        words = title.lower().split()
        for word in word_list:
            if word in words:
                counts[word] = counts.get(word, 0) + words.count(word)

    after = sub_info.json().get("data").get("after")
    if after:
        count_words(subreddit, word_list, after, counts)
    else:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print("{}: {}".format(word, count))
