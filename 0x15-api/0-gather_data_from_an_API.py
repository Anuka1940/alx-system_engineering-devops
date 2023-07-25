#!/usr/bin/python3
"""return information about Employee TODO list by ID"""
import requests
import sys


def get_employee_todo(employee_id):
    """funtion to get employee to do list """
    base_url = "https://jsonplaceholder.typicode.com"
    employee_endpoint = f"{base_url}/users/{employee_id}"
    response = requests.get(employee_endpoint)

    if response.status_code != 200:
        print("Error: Employee ID not found or API request failed.")
        return
    employee_data = response.json()
    name = employee_data["name"]

    todo_endpoint = f"{base_url}/todos?userId={employee_id}"
    response = requests.get(todo_endpoint)

    if response.status_code != 200:
        print("Error: TODO list not found or API request failed.")
        return

    todo_list = response.json()
    todos = len(todo_list)
    finished = [task for task in todo_list if task["completed"]]

    print(f"Employee {name} is done with tasks({len(finished)}/{todos}):")
    for task in finished:
        print(f"\t{task['title']}")


if len(sys.argv) != 2:
    print("Usage: python script.py employee_id")
else:
    employee_id = int(sys.argv[1])
    get_employee_todo(employee_id)
