#!/usr/bin/python3
# extend to export data in csv format

import csv
import json
import requests
import sys


def get_user_list():
    emp_id = int(sys.argv[1])
    url_1 = 'https://jsonplaceholder.typicode.com/users/%s' % emp_id
    url_2 = '%s/todos' % url_1
    list_todos = requests.get(url_2).json()
    usr = requests.get(url_1).json()
    path = "{}.csv".format(emp_id)

    with open(path, 'w', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)
        for todos in list_todos:
            writer.writerow([emp_id, usr.get('username'),
                            todos.get('completed'), todos.get('title')])


if __name__ == '__main__':
    list_todos = get_user_list()
