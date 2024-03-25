#!/usr/bin/python3
"""gathers data from an API and present it
"""
import requests
import sys


if __name__ == "__main__":
    id = int(sys.argv[1])

    with requests.get(f"https://jsonplaceholder.typicode.com/users/{id}") as resp:
        name = resp.json().get('name')

    url = f"https://jsonplaceholder.typicode.com/users/{id}/todos"
    with requests.get(url) as resp:
        todos = resp.json()

    completed = [todo for todo in todos if todo.get('completed') is True]
    print(f"Employee {name} is done with tasks({len(completed)}/{len(todos)}):")
    for todo in completed:
        print(f"\t {todo.get('title')}")
