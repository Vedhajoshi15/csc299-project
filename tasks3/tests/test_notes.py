import os, json
from tasks3 import add_note, search_notes, load_notes

def setup_function():
    # reset notes.json before each test
    if os.path.exists("notes.json"):
        os.remove("notes.json")

def test_add_note_creates_file_and_saves():
    add_note("AI", "Artificial Intelligence")
    data = load_notes()
    assert len(data) == 1
    assert data[0]["title"] == "AI"
    assert data[0]["content"] == "Artificial Intelligence"

def test_search_notes_finds_keyword():
    add_note("Python", "Scripting examples")
    results = search_notes("python")
    assert len(results) == 1
    assert results[0]["title"] == "Python"
