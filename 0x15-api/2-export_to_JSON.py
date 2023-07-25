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
        user_name = user[0].get('username')

        todos = r.get('{}todos?userId={}'.format(url, user_id)).json()

        data = []
        for task in todos:
            data_dict = {}
            data_dict.update({
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": user_name})
            data.append(data_dict)

        with open("{}.json".format(user_id), 'w') as json_file:
            json.dump(data, json_file)
