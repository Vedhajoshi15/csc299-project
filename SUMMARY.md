SUMMARY: Development of the Tasks5 Project Using Spec-Driven Development

This document summarizes the full development process of my CSC299 final project, “tasks5,” built using GitHub’s Spec-Kit and supported by AI coding assistance (GitHub Copilot and ChatGPT). The project followed a structured, multi-phase workflow: Constitution → Specification → Plan → Tasks → Implementation. This summary details how each phase was completed, how AI tools were incorporated, what worked well, what challenges I encountered, and what I learned throughout the process.

1. Project Overview

The goal of tasks5 was to build a command-line task management system in Python. The system supports adding tasks, listing tasks, searching tasks, and storing all data persistently in JSON format. The project emphasizes clarity, simplicity, and extensibility. Unlike earlier prototypes (tasks1 and tasks4), tasks5 was developed using a rigorous Spec-Driven Development methodology to simulate real-world engineering workflows.

2. Constitution Phase

The first phase involved creating a project constitution using GitHub Copilot inside VS Code. This constitution defined the guiding principles for the project, including:

The system must be a CLI-based task manager written in Python

JSON must be used for persistent storage

Commands must include add/list/search (with optional delete/complete/show)

The project must remain simple, readable, and easy to extend

AI coding assistance must be documented

Development must follow the Spec-Kit pipeline strictly

This phase set the foundation for all future decisions. The constitution was saved to .specify/constitution.md.

3. Specification Phase

Next, I generated the full system specification (spec/spec.md). This document outlined:

The project’s purpose and high-level design

All supported commands and their expected behavior

Data model for tasks (id, description, timestamp, completed flag, tags)

Example CLI usage

Input/output formats

JSON file structure

Error handling requirements

Testing expectations

This step was crucial because it forced me to think about the behavior before writing any code. Copilot helped draft the initial structure, and I refined it based on the assignment’s requirements.

4. Planning Phase

The third stage was producing the implementation plan (spec/plan.md). This document translated the specification into a clear development roadmap. It included:

Architecture overview (src/tasks5/* structure)

Module responsibilities (models.py, storage.py, cli.py, commands/*)

How the CLI argument parser should work

How storage should safely read/write JSON

Testing plan for each component

Phase-by-phase implementation sequence

This plan acted as a blueprint for the entire implementation. It also prevented me from jumping into code too early.

5. Tasks Breakdown Phase

In this phase, I generated a list of small, actionable development tasks (spec/tasks.md). This included:

Creating the project folder structure

Implementing the Task dataclass

Adding JSON storage with load/save/add logic

Building the CLI router and subcommands

Writing unit tests for storage and commands

Designing integration tests

Creating documentation updates

Breaking everything down into small tasks helped keep the project organized and manageable.

6. Implementation Phase

Following the plan and task list, I instructed Copilot to scaffold the entire project. Copilot generated:

Source code:
src/tasks5/__init__.py
src/tasks5/cli.py
src/tasks5/models.py
src/tasks5/storage.py
src/tasks5/commands/add.py
src/tasks5/commands/list.py
src/tasks5/commands/search.py

Tests:
tests/test_storage.py
tests/test_commands.py

Data file:
tasks.json


The generated code matched the specification:

models.py implemented the Task structure

storage.py handled JSON persistence

Subcommand modules handled add, list, and search logic

The CLI used argparse to route commands

After scaffolding, I reviewed and refined the code manually to ensure it aligned with the constitution and specification.

7. AI Assistance Reflection

Both GitHub Copilot and ChatGPT were essential throughout the project.

What worked well:

Copilot handled scaffolding quickly and accurately

ChatGPT was extremely helpful guiding the workflow and generating specification-level documents

AI helped maintain consistency across modules

AI-generated tests helped catch early storage issues

What did NOT work or caused difficulties:

Spec-Kit commands do not run in terminal; they must be executed in Copilot Chat

Some prompt files were empty, requiring manual direction

Copilot sometimes guessed folder names incorrectly, requiring adjustments

Occasionally, the assistant needed clarification to match the CSC299 grading rubric

Lessons learned:

Spec-Driven Development is much easier when the “thinking work” is done before any coding begins

AI tools are powerful but must be guided precisely

Clear specifications prevent confusion and re-work

Commit history matters — small, meaningful commits help track progress

8. Final Repository Preparation

After implementation, I copied everything (except the .git folder) into csc299-project/tasks5/ as required. I committed the changes with descriptive messages and documented AI usage. The commit history clearly shows the Spec-Kit workflow.

9. Conclusion

This project taught me how to work systematically using specifications, plans, and structured development steps. It also showed me how AI tools can support — but not replace — real engineering judgment. The result is a clean, extensible, professional-grade CLI task manager that meets all CSC299 requirements and reflects a full spec-driven development lifecycle.
