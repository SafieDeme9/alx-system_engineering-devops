#!/usr/bin/python3
"""
script that returns information about his/her TODO list progress
for given employee ID.
"""
import requests as r
import sys

user_id = sys.argv[1]
url = 'https://jsonplaceholder.typicode.com/'

if __name__ == "__main__":
    user = r.get('{}users?id={}'.format(url, user_id)).json()
    user_name = user[0].get('name')

    todos = r.get('{}todos?userId={}'.format(url, user_id)).json()
    all_tasks = len(todos)
    tasks_done = 0

    for task in todos:
        if task.get('completed'):
            tasks_done += 1
    print(
            'Employee {} is done with tasks({}/{}):'
            .format(user_name, tasks_done, all_tasks))
    for task in todos:
        if task.get('completed'):
            print('\t {}'.format(task.get('title')))
