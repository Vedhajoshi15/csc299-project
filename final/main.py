import json
import os

# ---------- TASK MANAGEMENT ----------
def add_task():
    task_name = input("Enter task name: ")
    task = {"name": task_name}

    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
    else:
        tasks = []

    tasks.append(task)

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
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task['name']}")


# ---------- PKMS (NOTES) ----------
def add_note():
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    note = {"title": title, "content": content}

    if os.path.exists("notes.json"):
        with open("notes.json", "r") as f:
            notes = json.load(f)
    else:
        notes = []

    notes.append(note)

    with open("notes.json", "w") as f:
        json.dump(notes, f, indent=4)

    print(f"Note '{title}' added!")


def list_notes():
    if not os.path.exists("notes.json"):
        print("No notes found.")
        return

    with open("notes.json", "r") as f:
        notes = json.load(f)

    if not notes:
        print("No notes to show.")
    else:
        print("\nYour Notes:")
        for i, note in enumerate(notes, 1):
            print(f"{i}. {note['title']}: {note['content']}")

def ai_agent():
    notes_count = 0
    tasks_count = 0
    keywords = {}

    # Count tasks
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
            tasks_count = len(tasks)

            for t in tasks:
                for word in t["name"].lower().split():
                    keywords[word] = keywords.get(word, 0) + 1

    # Count notes
    if os.path.exists("notes.json"):
        with open("notes.json", "r") as f:
            notes = json.load(f)
            notes_count = len(notes)

            for n in notes:
                for word in (n["title"] + " " + n["content"]).lower().split():
                    keywords[word] = keywords.get(word, 0) + 1

    print("\n--- AI Summary Report ---")
    print(f"Total Tasks: {tasks_count}")
    print(f"Total Notes: {notes_count}")

    if keywords:
        print("\nMost Frequent Words:")
        for w in sorted(keywords, key=keywords.get, reverse=True)[:5]:
            print(f"  {w} ({keywords[w]} times)")
    else:
        print("No keywords found yet.")

    print("\nAI Suggestion:")
    if tasks_count == 0 and notes_count == 0:
        print("You haven’t added anything yet. Start by adding tasks or notes!")
    elif tasks_count > notes_count:
        print("You seem focused on tasks. Maybe summarize your progress in a note!")
    elif notes_count > tasks_count:
        print("Lots of notes! Try converting some into actionable tasks.")
    else:
        print("Great balance between notes and tasks — keep it up!")


# ---------- MAIN CHAT LOOP ----------
print("\nWelcome to your AI-based Knowledge & Task Manager!")
print("Type commands like:\n")
print("  'add task'")
print("  'list tasks'")
print("  'add note'")
print("  'list notes'")
print("  'help'")
print("  'exit'")

while True:
    command = input("\n> ").lower().strip()

    if command == "add task":
        add_task()
    elif command == "list tasks":
        list_tasks()
    elif command == "add note":
        add_note()
    elif command == "list notes":
        list_notes()
    elif command == "ai agent":
        ai_agent()    
    elif command == "help":
        print("\nCommands available:")
        print("  add task     - add a new task")
        print("  list tasks   - show all tasks")
        print("  add note     - add a new note")
        print("  list notes   - show all notes")
        print("  ai agent     - analyze your notes and tasks ")
        print("  exit         - quit the program")
    elif command == "exit":
        print("Goodbye!")
        break
    else:
        print("Unknown command. Type 'help' for options.")
