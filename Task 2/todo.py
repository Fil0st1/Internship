import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r", encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f]

def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        for t in tasks:
            f.write(t + "\n")

tasks = load_tasks()

while True:

    task = []
    print("--- To-Do List Manager ---")
    print("1. Add a new task")
    print("2. remove a task")
    print("3. View all tasks")

    choice = input("Choose an option (1-3) or 'q' to quit: ")
    if choice == 'q':
        print("Goodbye!")
        break
    if choice == '1':
        new_task = input("Enter the new task: ")
        if new_task:
            tasks.append(new_task)
            save_tasks(tasks)
            print(f"Task '{new_task}' added.")
        else:
            print("Empty task not added.")
    elif choice == '2':
        if not tasks:
            print("No tasks to remove.")
            continue
        print("Tasks:")
        for i, t in enumerate(tasks, start=1):
            print(f"{i}. {t}")
        idx = input("Enter the task number to remove (or 'c' to cancel): ").strip().lower()
        if idx == 'c':
            continue
        try:
            idx = int(idx)
            if 1 <= idx <= len(tasks):
                removed = tasks.pop(idx - 1)
                save_tasks(tasks)
                print(f"Removed task: {removed}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
    elif choice == '3':
        if not tasks:
            print("No tasks found.")
        else:
            print("Your tasks:")
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t}")
    else:
        print("Invalid option. Please choose 1-3 or 'q' to quit.")
