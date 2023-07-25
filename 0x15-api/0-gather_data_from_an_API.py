#!/usr/bin/python3
"""return information about Employee TODO list by ID"""
import requests
import sys

def get_employee_todo(Employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    employee_endpoint = f"{base_url}/users/{employee_id}"
    response = requests.get(employee_endpoint)

    if response.status_code != 200:
        print("Error: Employee ID not found or API request failed.")
        return
    Employee_data = response.json()
    employee_name = Employee_data["name"]

    tode_endpoint = f"{base_url}/todos?userId={employee_id}"
    response = requests.get(tode_endpoint)
    
    if response.status_code != 200:
        print("Error: TODO list not found or API request failed.")
        return
    
    todo_list = response.json()
    total_tasks = len(todo_list)
    completed_tasks = [task for task in todo_list if task["completed"]]

    print(f"Employee {employee_name} is done with tasks ({len(completed_tasks)}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")
if len(sys.argv) != 2:
    print("Usage: python script.py employee_id")
else:
    employee_id = int(sys.argv[1])
    get_employee_todo(employee_id)
