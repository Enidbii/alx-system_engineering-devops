#!/usr/bin/python3
"""For a given employee ID, returns information about
their TODO list progress"""

import json
import requests
import sys


def get_user_list():
    emp_id = int(sys.argv[1])
    url_1 = 'https://jsonplaceholder.typicode.com/users/%s' % emp_id
    url_2 = '%s/todos' % url_1
    list_todos = requests.get(url_2).json()
    usr = requests.get(url_1).json()
    complete_list = []
    for todos in list_todos:
        if todos.get('completed') is True:
            complete_list.append(todos.get('title'))

    print("Employee {} is donemwith tasks({}/{}): "
          .format(usr.get('name'), len(complet_list), len(list_todos)))
    for todos in complete_list:
        print("\t {}".format(todos))


if __name__ == '__main__':
    list_todos = get_user_list()
