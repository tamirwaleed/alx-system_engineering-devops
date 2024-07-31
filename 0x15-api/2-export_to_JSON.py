#!/usr/bin/python3
''' Export to JSON '''

import csv
import json
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    emp_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(emp_id)).json()
    todo_param = {"userId": emp_id}
    todo = requests.get(url + "todos", params=todo_param).json()
    theFile = {emp_id: [{"task": x.get("title"),
                         "completed": x.get("completed"),
                         "username": user.get("username")}
               for x in todo]}
    filename = emp_id + ".json"
    with open(filename, "w", newline='') as fd:
        json.dump(theFile, fd)
