#!/usr/bin/python3
"""gathers data from an API and save it in JSON file
"""
import json
import requests


if __name__ == "__main__":
    url = f"https://jsonplaceholder.typicode.com/users/"
    with requests.get(url) as resp:
        users = resp.json()
    url = f"https://jsonplaceholder.typicode.com/todos"
    with requests.get(url) as resp:
        todos = resp.json()

    super_dict = {}
    for user in users:
        id = user.get('id')
        username = user.get('username')
        task_list = []
        userTodos = [todo for todo in todos if todo.get('userId') == id]
        for todo in userTodos:
            task_dict = {
                "username": username,
                "task": todo.get('title'),
                "completed": todo.get('completed')
            }
            task_list.append(task_dict)
        super_dict[f"{id}"] = task_list

    json_string = json.dumps(super_dict)

    with open(f"todo_all_employees.json", "w", encoding="utf-8") as f:
        f.write(json_string)
