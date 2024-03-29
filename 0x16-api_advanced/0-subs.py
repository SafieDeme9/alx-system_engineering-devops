#!/usr/bin/python3
"""function that returns the number of subscribers of a given subreddit"""
import requests

def number_of_subscribers(subreddit):
    url = f"https://reddit.com/r/{subreddit}/about.json"
    headers = {
            "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data["data"].get("subscribers")
    else:
        return 0
