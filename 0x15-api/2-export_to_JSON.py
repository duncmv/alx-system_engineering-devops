#!/usr/bin/python3
"""gathers data from an API and save it in JSON file
"""
import json
import requests
import sys

if __name__ == "__main__":
    id = int(sys.argv[1])
    url = f"https://jsonplaceholder.typicode.com/users/{id}"

    with requests.get(url) as resp:
        username = resp.json().get('username')

    url = f"https://jsonplaceholder.typicode.com/users/{id}/todos"
    with requests.get(url) as resp:
        todos = resp.json()

    task_list = []
    for todo in todos:
        task_dict = {
            "task": todo.get('title'),
            "completed": todo.get('completed'),
            "username": f"{username}"
        }
        task_list.append(task_dict)

    json_string = json.dumps({f"{id}": task_list})

    with open(f"{id}.json", "w", encoding="utf-8") as f:
        f.write(json_string)
