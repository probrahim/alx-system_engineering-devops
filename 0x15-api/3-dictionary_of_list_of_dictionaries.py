#!/usr/bin/python3
""" lists of employees"""

import json
import requests
import sys


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"

    repondre = requests.get(url)
    users = repondre.json()

    dictionary = {}
    for index in users:
        user_id = index.get('id')
        username = index.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
        url = url + '/todos/'
        response = requests.get(url)
        tasks = response.json()
        dictionary[user_id] = []
        for i in tasks:
            dictionary[user_id].append({
                "task": i.get('title'),
                "completed": i.get('completed'),
                "username": username
            })
    with open('todo_all_employees.json', 'w') as file:
        json.dump(dictionary, file)
