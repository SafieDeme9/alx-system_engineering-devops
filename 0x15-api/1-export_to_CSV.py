#!/usr/bin/python3
"""
script that returns information about his/her TODO list progress
for given employee ID.
"""

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

        with open('{}.csv'.format(user_id), 'w') as file:
            for task in todos:
                file.write(
                        '"{}","{}","{}","{}"\n'.format(
                            user_id,
                            user_name,
                            task.get('completed'),
                            task.get('title')))
