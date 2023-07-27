#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CVS format."""
import csv
import requests
import sys

if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    user_info = requests.get(base_url).json()
    username = user_info.get("username")
    tasks_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)
    tasks = requests.get(tasks_url).json()
    completed_tasks = [task for task in tasks if task.get("completed")]

    # Generating CSV file
    csv_file = "{}.csv".format(employee_id)
    with open(csv_file, mode="w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in completed_tasks:
            writer.writerow([employee_id, username, task["completed"], task["title"]])
