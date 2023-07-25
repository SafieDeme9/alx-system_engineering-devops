#!/usr/bin/python3
"""
script that returns information about his/her TODO list progress
for given employee ID.
"""

import json
import requests as r
import sys

url = 'https://jsonplaceholder.typicode.com/'
"""we took the url"""


if __name__ == "__main__":
    if len(sys.argv) > 1:
        user_id = sys.argv[1]
        user = r.get('{}users?id={}'.format(url, user_id)).json()
        user_name = user[0].get('name')

        todos = r.get('{}todos?userId={}'.format(url, user_id)).json()

        with open("{}.json".format(user_id), 'w') as json_file:
            data = list(map(
                lambda x: {
                    "task": x.get("title"),
                    "completed": x.get("completed"),
                    "username": user_name
                    },
                todos))
            data = {
                    "{}".format(user_id): data
            }
            json.dump(data, json_file)
