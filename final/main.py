import json
import os

# ---------------------------------------------
# Helper Functions
# ---------------------------------------------
def load_json(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as f:
        return json.load(f)

def save_json(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


# ---------------------------------------------
# TASK FUNCTIONS
# ---------------------------------------------
def add_task():
    name = input("Enter task name: ")
    tasks = load_json("tasks.json")
    tasks.append({"name": name})
    save_json("tasks.json", tasks)
    print(f"Task '{name}' added.")

def list_tasks():
    tasks = load_json("tasks.json")
    if not tasks:
        print("No tasks found.")
        return

    print("\nYour Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task['name']}")

def delete_task():
    tasks = load_json("tasks.json")
    if not tasks:
        print("No tasks to delete.")
        return

    list_tasks()
    num = input("\nEnter task number to delete: ")

    if not num.isdigit() or int(num) < 1 or int(num) > len(tasks):
        print("Invalid number.")
        return

    removed = tasks.pop(int(num) - 1)
    save_json("tasks.json", tasks)
    print(f"Deleted task: {removed['name']}")


# ---------------------------------------------
# NOTE FUNCTIONS
# ---------------------------------------------
def add_note():
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    notes = load_json("notes.json")
    notes.append({"title": title, "content": content})
    save_json("notes.json", notes)
    print(f"Note '{title}' added.")

def list_notes():
    notes = load_json("notes.json")
    if not notes:
        print("No notes found.")
        return

    print("\nYour Notes:")
    for i, note in enumerate(notes, 1):
        print(f"{i}. {note['title']}: {note['content']}")

def delete_note():
    notes = load_json("notes.json")
    if not notes:
        print("No notes to delete.")
        return

    list_notes()
    num = input("\nEnter note number to delete: ")

    if not num.isdigit() or int(num) < 1 or int(num) > len(notes):
        print("Invalid number.")
        return

    removed = notes.pop(int(num) - 1)
    save_json("notes.json", notes)
    print(f"Deleted note: {removed['title']}")


# -------------------------------------------------------
# OFFLINE AI SUMMARIZER (DeepSeek-style mock response)
# -------------------------------------------------------
def ai_agent():
    tasks_count = 0
    notes_count = 0
    keywords = {}

    # ----- Count tasks -----
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
            tasks_count = len(tasks)

            for t in tasks:
                for word in t["name"].lower().split():
                    keywords[word] = keywords.get(word, 0) + 1

    # ----- Count notes -----
    if os.path.exists("notes.json"):
        with open("notes.json", "r") as f:
            notes = json.load(f)
            notes_count = len(notes)

            for n in notes:
                combined = (n["title"] + " " + n["content"]).lower()
                for word in combined.split():
                    keywords[word] = keywords.get(word, 0) + 1

    # ----- Output full report -----
    print("\n--------- AI SUMMARY REPORT ---------")
    print(f"Total Tasks: {tasks_count}")
    print(f"Total Notes: {notes_count}")

    if keywords:
        print("\nTop Keywords:")
        for w in sorted(keywords, key=keywords.get, reverse=True)[:5]:
            print(f"  {w} ({keywords[w]} times)")
    else:
        print("\nNo keywords found yet.")

    print("\nAI Suggestion:")
    if tasks_count == 0 and notes_count == 0:
        print("You haven’t added anything yet. Start by adding tasks or notes!")
    elif tasks_count > notes_count:
        print("You seem focused on tasks. Maybe summarize your progress in a note!")
    elif notes_count > tasks_count:
        print("Lots of notes! Try converting some into actionable tasks.")
    else:
        print("Great balance between notes and tasks — keep it up!")

    print("------------------------------------\n")


# ---------------------------------------------
# MAIN MENU LOOP
# ---------------------------------------------
def show_menu():
    print("\n==============================")
    print(" AI Knowledge & Task Manager ")
    print("==============================")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Delete Task")
    print("4. Add Note")
    print("5. List Notes")
    print("6. Delete Note")
    print("7. AI Summarize Task")
    print("8. Exit")
    print("==============================")

while True:
    show_menu()
    choice = input("Choose an option (1-8): ").strip()

    if choice == "1":
        add_task()
    elif choice == "2":
        list_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        add_note()
    elif choice == "5":
        list_notes()
    elif choice == "6":
        delete_note()
    elif choice == "7":
        ai_agent()
    elif choice == "8":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Try again.")
