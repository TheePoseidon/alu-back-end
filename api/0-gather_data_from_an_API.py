#!/usr/bin/python3

"""
This script retrieves an employee's todo list from the JSONPlaceholder API,
calculates the number of completed tasks, and prints the employee's name,
the number of completed tasks, and the titles of the completed tasks.

The script takes the employee ID as a command-line argument and uses it to fetch
the employee's details and todo list from the JSONPlaceholder API.
"""

import requests
import sys

if __name__ == "__main__":
    """
    The main section of the script.
    """

    # Set the base URL for the JSONPlaceholder API
    BASE_URL = "https://jsonplaceholder.typicode.com/"

    # Get the employee ID from the command-line argument
    try:
        USER_ID = int(sys.argv[1])
    except IndexError:
        print("Please provide the employee ID as a command-line argument.")
        sys.exit(1)
    except ValueError:
        print("The employee ID must be an integer.")
        sys.exit(1)

    # Get the user details using the provided ID from the command-line argument
    response = requests.get(BASE_URL + f"users/{USER_ID}/")
    if response.status_code != 200:
        print(f"Failed to retrieve employee data for user ID {USER_ID}")
        sys.exit(1)

    employee = response.json()

    # Extract the employee's name
    EMPLOYEE_NAME = employee.get('name')
    if not EMPLOYEE_NAME:
        print(f"Employee name not found for user ID {USER_ID}")
        sys.exit(1)

    # Get the todo list for the employee
    todos_response = requests.get(BASE_URL + f"users/{USER_ID}/todos")
    if todos_response.status_code != 200:
        print(f"Failed to retrieve todo list for user ID {USER_ID}")
        sys.exit(1)

    todos = todos_response.json()

    # Calculate the number of completed tasks
    completed_tasks = [todo for todo in todos if todo.get('completed')]
    total_tasks = len(todos)
    num_completed_tasks = len(completed_tasks)

    # Print the employee's name, the number of completed tasks, and the total number of tasks
    print(f"Employee {EMPLOYEE_NAME} is done with tasks ({num_completed_tasks}/{total_tasks}):")

    # Print the titles of the completed tasks
    for task in completed_tasks:
        print(f"\t {task.get('title')}")
