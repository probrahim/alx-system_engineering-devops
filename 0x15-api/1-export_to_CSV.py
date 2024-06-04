#!/usr/bin/python3
"""  lists of employees API"""

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

    with open('{}.csv'.format(employeeId), 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'
                       .format(employeeId, username, task.get('completed'),
                               task.get('title')))
