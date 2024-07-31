#!/usr/bin/python3
''' Export to csv '''

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
    theFile = [["{}".format(emp_id), '{}'.format(user.get("name")), 
                '{}'.format(x.get("completed")), '{}'.format(x.get("title"))]
                for x in todo]
    filename = emp_id + ".csv"
    with open(filename, "w", newline = '') as fd:
        write_obj = csv.writer(fd)
        write_obj.writerows(theFile)
