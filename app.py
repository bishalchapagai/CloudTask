import json
from pathlib import Path

FILE = Path(__file__).resolve().parent / "tasks.json"


# LOAD TASKS
def load_tasks():
    if FILE.exists():
        try:
            with open(FILE, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            print("Could not load tasks. Starting with an empty list.")
    return []


# SAVE TASKS
def save_tasks():
    with open(FILE, "w") as file:
        json.dump(tasks, file, indent=4)


# CREATE
def add_task():
    task = input("Enter a new task: ").strip()

    if task:
        tasks.append(task)
        save_tasks()
        print("Task added and saved successfully!")
    else:
        print("Task cannot be empty.")


# READ
def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("\nYour Tasks:")

    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")


# UPDATE
def update_task():
    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter task number to update: "))

        if 1 <= number <= len(tasks):
            new_task = input("Enter updated task: ").strip()

            if new_task:
                tasks[number - 1] = new_task
                save_tasks()
                print("Task updated and saved!")
            else:
                print("Task cannot be empty.")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


# DELETE
def delete_task():
    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter task number to delete: "))

        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            save_tasks()
            print(f"Deleted task: {removed}")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


# MAIN APPLICATION
def main():
    while True:
        print("\n====== CloudTask Manager ======")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


tasks = load_tasks()

if __name__ == "__main__":
    main()