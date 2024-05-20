#!/usr/bin/python3
""" This script uses a rest api to fetch the information
    about an employee todo list
"""
import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + "users/{}".format(id)).json()
    todos = requests.get(url + "todos", params={"userId": id}).json()
    todos_complete = []
    for todo in todos:
        if todo.get("completed"):
            todos_complete.append(todo)
    print("Employee {} is done with tasks({}/{}):".format(
        user.get('name'), len(todos_complete), len(todos)))
    for todo in todos_complete:
        print("\t {}".format(todo.get('title')))
