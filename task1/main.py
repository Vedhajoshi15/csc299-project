import json
import os
import sys

TASK_FILE = "tasks.json"

def load_tasks():
    """Load existing tasks from the JSON file."""
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(task_name):
    """Add a new task."""
    tasks = load_tasks()
    tasks.append({"name": task_name})
    save_tasks(tasks)
    print(f"✅ Task added: {task_name}")

def list_tasks():
    """List all tasks."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    print("\nYour tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task['name']}")

def search_tasks(keyword):
    """Search tasks by keyword."""
    tasks = load_tasks()
    matches = [t for t in tasks if keyword.lower() in t["name"].lower()]
    if not matches:
        print(f"No tasks found matching '{keyword}'.")
    else:
        print(f"\nTasks matching '{keyword}':")
        for i, task in enumerate(matches, 1):
            print(f"{i}. {task['name']}")

def show_help():
    print("""
Usage:
  python main.py add "task name"      → Add a new task
  python main.py list                 → List all tasks
  python main.py search "keyword"     → Search tasks
  python main.py help                 → Show this help message
""")

def main():
    if len(sys.argv) < 2:
        show_help()
        return

    command = sys.argv[1].lower()

    if command == "add" and len(sys.argv) > 2:
        add_task(" ".join(sys.argv[2:]))
    elif command == "list":
        list_tasks()
    elif command == "search" and len(sys.argv) > 2:
        search_tasks(" ".join(sys.argv[2:]))
    elif command == "help":
        show_help()
    else:
        print("Invalid command.\n")
        show_help()

if __name__ == "__main__":
    main()
