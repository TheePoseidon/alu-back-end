#!/usr/bin/python3

"""
This script retrieves an employee's todo list from the JSONPlaceholder API,
 calculates the number
 of completed tasks,
and prints the employee's name, the number of completed tasks, and the titles
 of the completed tasks.

The script takes the employee ID as a command-line argument and uses
 it to fetch the employee's details and todo list fr
the JSONPlaceholder API.
"""
import requests
import sys


if __name__ == "__main__":
    """
    The main section of the script.
    """

    # Set the base URL for the JSONPlaceholder API
    BASE_URL = "https://jsonplaceholder.typicode.com/"

    try:
        USER_ID = int(sys.argv[1])
    except IndexError:
        print("Please provide the employee ID as a command-line argument.")
        sys.exit(1)
    except ValueError:
        print("The employee ID must be an integer.")
        sys.exit(1)

    # Get the user details using the provided ID from the command-line argument
    employees = requests.get(BASE_URL + f"/users/{USER_ID}/").json()

    # Extract the employee's name
    EMPLOYEE_NAME = employees.get('name')

    # Get the todo list for the employee
    EMPLOY_TODO = requests.get(BASE_URL + f"/users/{USER_ID}/todos").json()

    # Initialize a dictionary to store the todo items and their completion
    # status
    TOTAL_NUMBER_OF_TASKS = {}

    # Iterate through the todo list and add the title and completion status to
    # the dictionary
    for todo in EMPLOY_TODO:
        TOTAL_NUMBER_OF_TASKS.update(
            {todo.get("title"): todo.get("completed")})

    # Calculate the number of completed tasks
    NUMBER_OF_DONE_TASKS = len(
        [k for k, v in TOTAL_NUMBER_OF_TASKS.items() if v is True])

    # Print the employee's name, the number of completed tasks, and the total
    # number of tasks
    print("Employee {} is done with tasks({}/{}): ".format(EMPLOYEE_NAME,
          NUMBER_OF_DONE_TASKS, len(TOTAL_NUMBER_OF_TASKS)))

    # Iterate through the todo list and print the titles of the completed tasks
    for key, val in TOTAL_NUMBER_OF_TASKS.items():
        if val is True:
            print("\t {}".format(key))
