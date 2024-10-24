#!/usr/bin/python3

"""
This script retrieves the todo lists for all employees from
the JSONPlaceholder API,
and exports the data in a JSON file.

The resulting JSON file will have the following structure:
{
  "USER_ID": [
    {
      "username": "USERNAME",
      "task": "TASK_TITLE",
      "completed": TASK_COMPLETED_STATUS
    },
    {
      "username": "USERNAME",
      "task": "TASK_TITLE",
      "completed": TASK_COMPLETED_STATUS
    },
    ...
  ],
  "USER_ID": [
    {
      "username": "USERNAME",
      "task": "TASK_TITLE",
      "completed": TASK_COMPLETED_STATUS
    },
    {
      "username": "USERNAME",
      "task": "TASK_TITLE",
      "completed": TASK_COMPLETED_STATUS
    },
    ...
  ]
}
"""
import json
import requests

if __name__ == "__main__":
    """
    The main section of the script.
    """

    # Set the base URL for the JSONPlaceholder API
    BASE_URL = "https://jsonplaceholder.typicode.com/"

    # Get the list of all employees
    all_employees = requests.get(BASE_URL + "users").json()

    # Initialize the JSON data structure
    json_data = {}

    # Iterate through the list of employees
    for employee in all_employees:
        USER_ID = employee.get("id")
        USERNAME = employee.get("username")

        # Get the todo list for the current employee
        employee_todos = requests.get(
            BASE_URL + f"users/{USER_ID}/todos").json()

        # Add the employee's todo list to the JSON data structure
        json_data[USER_ID] = []
        for todo in employee_todos:
            json_data[USER_ID].append({
                "username": USERNAME,
                "task": todo.get("title"),
                "completed": todo.get("completed")
            })

    # Export the data to a JSON file
    json_file_name = "todo_all_employees.json"
    with open(json_file_name, 'w') as json_file:
        json.dump(json_data, json_file, indent=2)
