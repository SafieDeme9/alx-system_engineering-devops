#!/usr/bin/python3
"""function that prints top 10 hottest post of given subreddit"""
import requests


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
            "User-Agent": "Mozilla/5.0"
    }
    params = {
            "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
            allow_redirects=False)
    if response.status_code == 200:
        posts = response.json()
        children = posts["data"]["children"]
        for i in range(10):
            print(children[i]["data"]["title"])
    else:
        print("None")
