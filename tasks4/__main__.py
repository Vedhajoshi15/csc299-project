"""
tasks4 - Standalone experiment simulating OpenAI Chat Completions API
This version runs entirely offline and demonstrates the required logic.
"""

def summarize_tasks(use_api=False):
    """Summarize multiple paragraph-length descriptions."""
    descriptions = [
        """Develop a Python program that reads a CSV file of student grades,
        calculates averages for each student, and outputs a report of top performers.""",

        """Design a small web app for tracking daily habits, showing user progress,
        and sending reminders for missed goals."""
    ]

    print("Summarizing tasks...\n")

    if use_api:
        print("Real API mode is disabled for this demo (no OpenAI access).")
    else:
        for i, desc in enumerate(descriptions, 1):
            summary = f"Task {i} Summary: {desc.split('.')[0][:45]}..."
            print(summary)
            print("-" * 60)

if __name__ == "__main__":
    summarize_tasks(use_api=False)
