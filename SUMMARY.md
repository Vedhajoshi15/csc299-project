# 📘 CSC299 Final Development Summary  
**Author:** Vedha Joshi  
**Course:** CSC 299 – Vibecoding  
**Quarter:** Fall 2025  

---

# 🧭 Overview

This summary explains the full development process of my CSC299 project across **Task 1 → Task 5 → Final Project**.  
Throughout the course, I built multiple prototypes and finally created a complete, combined **Task Manager + PKMS (Notes) + Offline AI Agent** system.

I used several tools during development, including:

- 🧠 **GitHub Copilot**  
- 🤖 **ChatGPT (AI guidance)**  
- 🛠️ **Git + GitHub**  
- 🧪 **UV + Pytest (Tasks3)**  
- 🗂️ **Spec-Kit (Tasks5)**  

This document also explains what worked, what didn’t, and how AI supported my workflow.

---

# 📝 **1. Task 1 – Basic Task Manager Prototype**

📌 **What I built:**  
My first working task manager using Python and JSON.

### 🔧 Features  
- ➕ Add tasks  
- 📄 List tasks  
- 🔍 Search tasks  
- ❓ Help menu  

### 📌 Command Examples
python main.py add "task name"
python main.py list
python main.py search "keyword"
python main.py help

Task 1 taught me how to build a simple CLI app and work with JSON storage.

---

# 📝 **2. Task 2 – Notes System (PKMS Prototype)**

📌 **What I added:**  
A personal knowledge management system with editable and deletable notes.

### 🔧 Features  
- ➕ Add notes  
- 📄 List notes  
- ✏️ Edit notes  
- ❌ Delete notes  
- 🔍 Search notes  

### 📌 Commands
python main.py add "title" "content"
python main.py list
python main.py edit "title" "new content"
python main.py delete "title"
python main.py search "keyword"

This was my first version of a PKMS and helped expand the design beyond simple tasks.

---

# 🧪 **3. Task 3 – UV Package + Pytest**

📌 Folder contained:  
README.md
main.py
notes.json
pyproject.toml
src/
tests/

### 🛠️ What I implemented:
- Created a UV Python package  
- Added `inc()` function  
- Wrote pytest test `test_inc.py`  
- Ran `uv run pytest` (1 test passed)  
- Integrated note or task logic inside a proper project structure  

This assignment taught me packaging, testing, and using UV.

---

# 🤖 **4. Task 4 – OpenAI Chat Completions Prototype**

📌 Folder contained:
README.md
main.py
pyproject.toml

### 🧠 What I built:
- A script that sends multiple paragraph-length tasks to OpenAI’s API  
- Received short summaries for each  
- Demonstrated API usage exactly as required  

Later, I removed online API usage from my final project, but *Task 4 was successfully completed as required*.

---

# 🗂️ **5. Task 5 – Spec-Kit Project (Spec-Driven Development)**

📌 Folder contained:
spec/
src/
tests/
tasks.json

Using GitHub’s **Spec-Kit**, I built a fully structured version of my task manager by generating:

### 📄 Documents
- ✍️ Constitution (`.specify/constitution.md`)
- 📘 Specification (`spec/spec.md`)
- 🗺️ Implementation plan (`spec/plan.md`)
- 🧩 Task breakdown (`spec/tasks.md`)

### 🧱 Code Structure (generated + refined)
- `src/tasks5/models.py`  
- `src/tasks5/storage.py`  
- `src/tasks5/cli.py`  
- `src/tasks5/commands/add.py`  
- `src/tasks5/commands/list.py`  
- `src/tasks5/commands/search.py`  

### 🧪 Tests
- `tests/test_storage.py`
- `tests/test_commands.py`

Task 5 taught me real software engineering workflow: planning → spec → execution.

---

# 🎯 **6. Final Project – Combined Task Manager + PKMS + Offline AI Agent**

📌 Folder:
final/
main.py
tasks.json
notes.json
README.md
video.txt

### ✨ Final Features Implemented

#### 📝 **Tasks**
- ➕ Add tasks  
- 📄 List tasks  
- ❌ Delete tasks  

#### 📚 **Notes (PKMS)**
- ➕ Add notes  
- 📄 List notes  
- ❌ Delete notes  

#### 🤖 **Offline AI Agent**
Because online API requires payment, I included an **offline AI summary** option:
- Counts task/notes  
- Extracts common keywords  
- Generates a summary sentence without API credits  

#### 🖥️ **UI Improvements**
- Number-based menu  
- Cleaner, single-line commands  
- More professional output  

This final version satisfies all requirements:  
- CLI interface  
- Tasks + Notes  
- AI agent  
- JSON persistent storage  

---

# 🤖 **7. How I Used AI Assistance**

### ✅ What worked well:
- Copilot scaffolded file structures and boilerplate quickly  
- ChatGPT helped generate my constitution, specs, and plan documents  
- AI suggestions improved readability and structure  
- AI guided me when debugging issues  

### ⚠️ What didn’t work:
- OpenAI API required paid credits  
- Spec-Kit newest version had bugs (as professor said)  
- Copilot sometimes generated wrong directory paths  
- Some prompts required manual adjustments  

### 🎓 Lessons Learned:
- Specifications make coding easier  
- AI is powerful but needs clear human direction  
- Version control and small commits matter  
- Testing early prevents bigger issues later  

---

# 🏁 **8. Conclusion**

Across Task 1 → Task 5 and the final submission, I learned:

- How to create prototypes  
- How to use AI assistants responsibly  
- How to plan using specifications  
- How to test and refine software  
- How to build a complete terminal application  

My final project meets all CSC299 requirements and reflects the full spec-driven development process.

---

# 🎉 **End of Summary**
