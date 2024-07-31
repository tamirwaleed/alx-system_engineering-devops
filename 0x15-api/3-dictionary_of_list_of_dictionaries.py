#!/usr/bin/python3
''' Export to JSON '''

import csv
import json
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    user = requests.get(url + "users").json()
    theFile = {}
    for use in user:
        todo_param = {"userId": use.get("id")}
        todo = requests.get(url + "todos", params=todo_param).json()
        theFile[use.get("id")] = [{"user": use.get("username"),
                                   "task": x.get("title"),
                                   "completed": x.get("completed")}
                                  for x in todo]
    filename = "todo_all_employees.json"
    with open(filename, "w", newline='') as fd:
        json.dump(theFile, fd)
