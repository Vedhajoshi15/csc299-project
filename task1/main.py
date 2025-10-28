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

def list_tasks():
    if not os.path.exists("tasks.json"):
        print("No tasks found.")
        return

    with open("tasks.json", "r") as f:
        tasks = json.load(f)

    if not tasks:
        print("No tasks to show.")
    else:
        print("Your tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task['name']}")


# Main program loop
while True:
    print("\n1. Add task")
    print("2. List tasks")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        list_tasks()
    elif choice == "3":
        break
    else:
        print("Invalid choice, try again.")

