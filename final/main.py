import json
import os

# ---------- Helper functions for loading/saving JSON ----------

def load_json(path):
    if not os.path.exists(path):
        return []
    try:
        with open(path, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        # If the file is corrupted, start fresh instead of crashing
        print(f"Warning: {path} is not valid JSON. Starting with an empty list.")
        return []


def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)


# ---------- TASK MANAGEMENT ----------

def add_task():
    task_name = input("Enter task name: ").strip()
    if not task_name:
        print("Task name cannot be empty.")
        return

    tasks = load_json("tasks.json")
    task = {"name": task_name}
    tasks.append(task)

    save_json("tasks.json", tasks)
    print(f"Task '{task_name}' added!")


def list_tasks():
    tasks = load_json("tasks.json")

    if not tasks:
        print("No tasks to show.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task['name']}")


def delete_task():
    tasks = load_json("tasks.json")

    if not tasks:
        print("No tasks to delete.")
        return

    print("\nYour Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task['name']}")

    choice = input("Enter task number to delete: ").strip()
    if not choice.isdigit():
        print("Invalid input.")
        return

    index = int(choice)
    if 1 <= index <= len(tasks):
        deleted = tasks.pop(index - 1)
        save_json("tasks.json", tasks)
        print(f"Deleted task: {deleted['name']}")
    else:
        print("Invalid task number.")


# ---------- PKMS (NOTES) ----------

def add_note():
    title = input("Enter note title: ").strip()
    content = input("Enter note content: ").strip()

    if not title and not content:
        print("Note cannot be completely empty.")
        return

    notes = load_json("notes.json")
    note = {"title": title, "content": content}
    notes.append(note)

    save_json("notes.json", notes)
    print(f"Note '{title or '(untitled)'}' added!")


def list_notes():
    notes = load_json("notes.json")

    if not notes:
        print("No notes to show.")
    else:
        print("\nYour Notes:")
        for i, note in enumerate(notes, 1):
            title = note["title"] or "(untitled)"
            print(f"{i}. {title}: {note['content']}")


def delete_note():
    notes = load_json("notes.json")

    if not notes:
        print("No notes to delete.")
        return

    print("\nYour Notes:")
    for i, note in enumerate(notes, 1):
        title = note["title"] or "(untitled)"
        print(f"{i}. {title}")

    choice = input("Enter note number to delete: ").strip()
    if not choice.isdigit():
        print("Invalid input.")
        return

    index = int(choice)
    if 1 <= index <= len(notes):
        deleted = notes.pop(index - 1)
        save_json("notes.json", notes)
        print(f"Deleted note: {deleted['title'] or '(untitled)'}")
    else:
        print("Invalid note number.")


# ---------- AI AGENT (offline, smarter) ----------

def ai_agent():
    tasks = load_json("tasks.json")
    notes = load_json("notes.json")

    tasks_count = len(tasks)
    notes_count = len(notes)
    keywords = {}

    # Collect words from tasks
    for t in tasks:
        for word in t.get("name", "").lower().split():
            keywords[word] = keywords.get(word, 0) + 1

    # Collect words from notes
    for n in notes:
        text = (n.get("title", "") + " " + n.get("content", "")).lower()
        for word in text.split():
            keywords[word] = keywords.get(word, 0) + 1

    print("\n--- AI Summary Report ---")
    print(f"Total Tasks: {tasks_count}")
    print(f"Total Notes: {notes_count}")

    if keywords:
        print("\nMost Frequent Words:")
        for w in sorted(keywords, key=keywords.get, reverse=True)[:5]:
            print(f"  {w} ({keywords[w]} times)")
    else:
        print("\nNo keywords found yet. Add some tasks or notes first.")

    # Smarter suggestions based on content
    print("\nAI Suggestions:")

    if tasks_count == 0 and notes_count == 0:
        print("- You haven’t added any tasks or notes yet. Start by adding a task like 'Finish homework' or a note about what you’re learning.")
        return

    # Content-based hints
    words = set(keywords.keys())

    if any(w in words for w in ["exam", "midterm", "final", "test"]):
        print("- You have study-related items. Consider creating a clear study plan and breaking it into small tasks.")
    if "project" in words:
        print("- You mentioned a project. Break the project into smaller, actionable steps and turn them into tasks.")
    if "python" in words:
        print("- You seem to be working with Python. Maybe add notes about errors you hit or patterns you learned.")
    if "ai" in words or "llm" in words or "model" in words:
        print("- You have AI-related content. Consider summarizing what you’ve learned so far in a dedicated note.")

    # Balance-based hint
    if tasks_count > notes_count:
        print("- You have more tasks than notes. You might want to write notes reflecting your progress or capturing ideas.")
    elif notes_count > tasks_count:
        print("- You have more notes than tasks. Try turning some of your notes into concrete, actionable tasks.")
    else:
        print("- You have a good balance between tasks and notes. Keep reviewing notes and completing tasks regularly.")

    # Urgency hint based on list length
    if tasks_count >= 5:
        print("- You have several tasks. Consider prioritizing the top 2–3 and focusing on them first.")
    elif tasks_count == 1:
        print("- You have one task. Try breaking it into smaller subtasks if it feels too big.")

    print("\n(These suggestions are generated offline by analyzing your current tasks and notes.)")


# ---------- MAIN CHAT LOOP ----------

print("\nWelcome to your AI-based Knowledge & Task Manager!")
print("Type commands like:\n")
print("  'add task'      - add a new task")
print("  'list tasks'    - show all tasks")
print("  'delete task'   - delete a task by number")
print("  'add note'      - add a new note")
print("  'list notes'    - show all notes")
print("  'delete note'   - delete a note by number")
print("  'ai agent'      - analyze your tasks and notes")
print("  'help'          - show commands")
print("  'exit'          - quit the program")

while True:
    command = input("\n> ").lower().strip()

    if command == "add task":
        add_task()
    elif command == "list tasks":
        list_tasks()
    elif command == "delete task":
        delete_task()
    elif command == "add note":
        add_note()
    elif command == "list notes":
        list_notes()
    elif command == "delete note":
        delete_note()
    elif command == "ai agent":
        ai_agent()
    elif command == "help":
        print("\nCommands available:")
        print("  add task      - add a new task")
        print("  list tasks    - show all tasks")
        print("  delete task   - delete a task by number")
        print("  add note      - add a new note")
        print("  list notes    - show all notes")
        print("  delete note   - delete a note by number")
        print("  ai agent      - analyze your notes and tasks")
        print("  exit          - quit the program")
    elif command == "exit":
        print("Goodbye!")
        break
    else:
        print("Unknown command. Type 'help' for options.")
