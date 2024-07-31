#!/usr/bin/python3
''' Export to csv '''

import json
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    emp_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(emp_id)).json()
    todo_param = {"userId": emp_id}
    todo = requests.get(url + "todos", params=todo_param).json()
    theFile = ""
    for x in todo:
        theFile += '"{}", "{}", "{}", "{}"\n'.format(emp_id, user.get("name"),
                                                     x.get("completed"),
                                                     x.get("title"))
    filename = emp_id + ".csv"
    with open(filename, "w") as fd:
        fd.write(theFile[:-1])
