#!/usr/bin/python3
""" lists of employees API """

import json
import requests
import sys


if __name__ == '__main__':
    employeeId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employeeId

    repondre = requests.get(url)
    username = repondre.json().get('username')

    todoUrl = url + "/todos"
    repondre = requests.get(todoUrl)
    tasks = repondre.json()

    dictionary = {employeeId: []}
    for i in tasks:
        dictionary[employeeId].append({
            "task": i.get('title'),
            "completed": i.get('completed'),
            "username": username
        })
    with open('{}.json'.format(employeeId), 'w') as filename:
        json.dump(dictionary, filename)
