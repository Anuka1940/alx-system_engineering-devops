#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to json  format."""
import json
import requests
import sys

if __name__ == "__main__":
    usr_id = int(sys.argv[1])
    b_url = "https://jsonplaceholder.typicode.com/"
    url = "https://jsonplaceholder.typicode.com/users/{}".format(usr_id)
    user_info = requests.get(url).json()
    username = user_info.get("username")
    t_url = b_url + "todos?userId={}".format(usr_id)
    tasks = requests.get(t_url).json()
    completed_tasks = [task for task in tasks if task.get("completed")]

    """Generating json data"""
    json_data = {(usr_id): [{"task": t.get("title"), "completed": t.get(
        "completed"), "username": username} for t in tasks]}

    """ Generating JSON file"""
    json_file = "{}.json".format(usr_id)
    with open(json_file, "w") as file:
        json.dump(json_data, file)
