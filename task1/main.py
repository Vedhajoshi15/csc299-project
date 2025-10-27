# Task 1 prototype
import json
import os

def add_task():
    task_name = input("Enter task name: ")
    task = {"name": task_name}

    # Load existing tasks
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
    else:
        tasks = []

    # Add new task
    tasks.append(task)

    # Save tasks back
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)

    print(f"Task '{task_name}' added!")
add_task()
