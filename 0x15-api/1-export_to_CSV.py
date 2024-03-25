#!/usr/bin/python3
"""gathers data from an API and save it in CSV file
"""
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
    csv_string = ""
    for todo in todos:
        status = todo.get('completed')
        title = todo.get('title')
        csv_string += f'"{id}","{username}","{status}","{title}"\n'

    with open(f"{id}.csv", "w", encoding="utf-8") as f:
        f.write(csv_string)
