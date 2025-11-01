import json
import os

def add_note():
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    note = {"title": title, "content": content}

    # Load existing notes
    if os.path.exists("notes.json"):
        with open("notes.json", "r") as f:
            notes = json.load(f)
    else:
        notes = []

    # Add the new note
    notes.append(note)

    # Save back to file
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


def search_notes():
    keyword = input("Enter a keyword to search: ").lower()

    if not os.path.exists("notes.json"):
        print("No notes found.")
        return

    with open("notes.json", "r") as f:
        notes = json.load(f)

    results = [note for note in notes if keyword in note["title"].lower() or keyword in note["content"].lower()]

    if results:
        print(f"\nFound {len(results)} matching note(s):")
        for i, note in enumerate(results, 1):
            print(f"{i}. {note['title']}: {note['content']}")
    else:
        print("No matching notes found.")

def edit_note():
    if not os.path.exists("notes.json"):
        print("No notes found.")
        return

    with open("notes.json", "r") as f:
        notes = json.load(f)

    if not notes:
        print("No notes to edit.")
        return

    # Show all notes
    print("\nYour Notes:")
    for i, note in enumerate(notes, 1):
        print(f"{i}. {note['title']}: {note['content']}")

    try:
        note_num = int(input("\nEnter the number of the note to edit: "))
        if 1 <= note_num <= len(notes):
            new_content = input("Enter new content for this note: ")
            notes[note_num - 1]["content"] = new_content

            # Save the updated notes
            with open("notes.json", "w") as f:
                json.dump(notes, f, indent=4)

            print(f"Note '{notes[note_num - 1]['title']}' updated successfully!")
        else:
            print("Invalid note number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_note():
    if not os.path.exists("notes.json"):
        print("No notes found.")
        return

    with open("notes.json", "r") as f:
        notes = json.load(f)

    if not notes:
        print("No notes to delete.")
        return

    print("\nYour Notes:")
    for i, note in enumerate(notes, 1):
        print(f"{i}. {note['title']}: {note['content']}")

    try:
        note_num = int(input("\nEnter the number of the note to delete: "))
        if 1 <= note_num <= len(notes):
            deleted = notes.pop(note_num - 1)

            # Save updated list
            with open("notes.json", "w") as f:
                json.dump(notes, f, indent=4)

            print(f"Note '{deleted['title']}' deleted successfully!")
        else:
            print("Invalid note number.")
    except ValueError:
        print("Please enter a valid number.")


# Main menu
while True:
    print("\n1. Add note")
    print("2. List notes")
    print("3. Search notes")
    print("4. Edit note")
    print("5. Delete note")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_note()
    elif choice == "2":
        list_notes()
    elif choice == "3":
        search_notes()
    elif choice == "4":
        edit_note()
    elif choice == "5":
        delete_note()
    elif choice == "6":
        break
    else:
        print("Invalid choice, try again.")
