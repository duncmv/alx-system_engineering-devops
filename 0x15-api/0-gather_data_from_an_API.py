#!/usr/bin/python3
"""gathers data from an API and present it
"""
import requests
import sys


if __name__ == "__main__":
    id = int(sys.argv[1])
    url = f"https://jsonplaceholder.typicode.com/users/{id}"
    with requests.get(url) as resp:
        name = resp.json().get('name')

    url = f"https://jsonplaceholder.typicode.com/users/{id}/todos"
    with requests.get(url) as resp:
        todos = resp.json()

    comp = [todo for todo in todos if todo.get('completed') is True]
    print(f"Employee {name} is done with tasks({len(comp)}/{len(todos)}):")
    for todo in comp:
        print(f"\t {todo.get('title')}")
