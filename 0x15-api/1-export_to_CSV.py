#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CVS format."""
import csv
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

    # Generating CSV file
    csv_file = "{}.csv".format(usr_id)
    with open(csv_file, mode="w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow(
                    [usr_id, username, task["completed"], task["title"]])
