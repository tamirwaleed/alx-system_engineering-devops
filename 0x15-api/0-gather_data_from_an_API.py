#!/usr/bin/python3
''' Gather Data from an API '''

import json
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    emp_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(emp_id)).json()
    todo_param = {"userId": emp_id}
    todo = requests.get(url + "todos", params=todo_param).json()
    completed = []
    for x in todo:
        if x.get("completed") is True:
            completed.append(x.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(user.get("name"),
                                                          len(completed),
                                                          len(todo)))
    for y in completed:
        print("\t {}".format(y))
