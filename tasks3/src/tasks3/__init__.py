import json, os

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
    return notes

def search_notes(keyword):
    notes = load_notes()
    return [n for n in notes if keyword.lower() in n["title"].lower() or keyword.lower() in n["content"].lower()]

def main():
    print("✅ Task 3: Note Manager ready. Run tests with `uv run pytest`.")
