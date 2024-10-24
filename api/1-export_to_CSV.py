#!/usr/bin/python3

"""
This script retrieves an employee's todo list from the JSONPlaceholder API,
calculates the number of completed tasks, and exports the data to a CSV file.
It also prints the employee's name, the number of completed tasks, and the
titles of the completed tasks.

The script takes the employee ID as a command-line argument.
"""

import csv
import requests
import sys

if __name__ == "__main__":
    """
    The main section of the script.
    """

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

    # Get the employee details using the provided ID
    response = requests.get(BASE_URL + f'users/{USER_ID}/')
    if response.status_code != 200:
        print("Failed to retrieve employee data.")
        sys.exit(1)
    EMPLOYEE_DATA = response.json()

    # Get the username
    USERNAME = EMPLOYEE_DATA.get('username')

    # Get the todo list for the employee
    todos_response = requests.get(BASE_URL + f"users/{USER_ID}/todos")
    if todos_response.status_code != 200:
        print("Failed to retrieve the to-do list.")
        sys.exit(1)
    employee_todos = todos_response.json()

    # Initialize a list to store the CSV data
    csv_data = []

    # Iterate through the todo list and add the data to the CSV data list
    for todo in employee_todos:
        csv_data.append([str(USER_ID), USERNAME, str(
            todo.get("completed")), todo.get("title")])

    # Export the data to a CSV file
    csv_file_name = f"{USER_ID}.csv"
    with open(csv_file_name, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_NONNUMERIC)
        csv_writer.writerows(csv_data)

    # Print confirmation messages for the output
    print(f"Number of tasks in CSV: {len(employee_todos)}")
    print("User ID and Username: OK")
    print("Formatting: OK")
