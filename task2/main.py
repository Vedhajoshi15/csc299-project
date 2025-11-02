import json
import os
import sys

NOTES_FILE = "notes.json"

def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r") as f:
            return json.load(f)
    return []

def save_notes(notes):
    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f, indent=4)

def add_note(title, content):
    notes = load_notes()
    notes.append({"title": title, "content": content})
    save_notes(notes)
    print(f"✅ Note added: {title}")

def list_notes():
    notes = load_notes()
    if not notes:
        print("No notes found.")
        return
    print("\nYour Notes:")
    for i, note in enumerate(notes, 1):
        print(f"{i}. {note['title']}: {note['content']}")

def search_notes(keyword):
    notes = load_notes()
    results = [n for n in notes if keyword.lower() in n["title"].lower() or keyword.lower() in n["content"].lower()]
    if not results:
        print(f"No notes found matching '{keyword}'.")
    else:
        print(f"\nNotes matching '{keyword}':")
        for i, note in enumerate(results, 1):
            print(f"{i}. {note['title']}: {note['content']}")
def edit_note(title, new_content):
    notes = load_notes()
    if not notes:
        print("  No notes found to edit.")
        return

    for note in notes:
        if note["title"].lower() == title.lower():
            old_content = note["content"]
            note["content"] = new_content
            save_notes(notes)
            print(f"  Note '{title}' updated successfully!")
            print(f"Old content: {old_content}")
            print(f"New content: {new_content}")
            return

    print(f" Note titled '{title}' not found. Use 'list' to see all available notes.")


def delete_note(title):
    notes = load_notes()
    if not notes:
        print("  No notes found to delete.")
        return

    for note in notes:
        if note["title"].lower() == title.lower():
            confirm = input(f"Are you sure you want to delete '{title}'? (y/n): ").lower()
            if confirm == "y":
                notes = [n for n in notes if n["title"].lower() != title.lower()]
                save_notes(notes)
                print(f"  Note '{title}' deleted successfully!")
            else:
                print("Deletion cancelled.")
            return

    print(f" Note titled '{title}' not found. Use 'list' to see all available notes.")

def show_help():
    print("""
Usage:
  python main.py add "title" "content"     → Add a new note
  python main.py list                      → List all notes
  python main.py search "keyword"          → Search notes
  python main.py edit "title" "new text"   → Edit an existing note
  python main.py delete "title"            → Delete a note
  python main.py help                      → Show this help message
""")

def main():
    if len(sys.argv) < 2:
        show_help()
        return

    command = sys.argv[1].lower()

    if command == "add" and len(sys.argv) >= 4:
        title = sys.argv[2]
        content = " ".join(sys.argv[3:])
        add_note(title, content)
    elif command == "list":
        list_notes()
    elif command == "search" and len(sys.argv) >= 3:
        keyword = " ".join(sys.argv[2:])
        search_notes(keyword)
    elif command == "edit" and len(sys.argv) >= 4:
        title = sys.argv[2]
        new_content = " ".join(sys.argv[3:])
        edit_note(title, new_content)
    elif command == "delete" and len(sys.argv) >= 3:
        title = " ".join(sys.argv[2:])
        delete_note(title)
   
    elif command == "help":
        show_help()
    else:
        print("Invalid command.\n")
        show_help()

if __name__ == "__main__":
    main()