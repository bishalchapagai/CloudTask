import json;
tasks = []
def load_tasks():
    global tasks;
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        print("No existing tasks found. Starting with an empty task list.")
def save_tasks():
    with open("tasks.json","w") as file:
        json.dump(tasks, file,indent =4);
    print("Tasks saved to tasks.json");

def add_task(task_name, priority_level):
    tasks.append({
        "task": task_name,
        "priority": priority_level,
        "status": "incomplete"
    })


def view_tasks():
    if not tasks:
        print("No Task Available")
    else:
        print("\n---Task List---")
        for index, t in enumerate(tasks, start=1):
            print(f"{index}. Task: {t['task']} / priority: {t['priority']} / status: {t['status']}")


def update_task():
    if not tasks:
        print("No task to Update")
        return
    else:
        view_tasks()
        try:
            task_index = int(input("Enter the task number to update: ")) - 1

            if 0 <= task_index < len(tasks):
                new_task_name = input("Enter new Task: ")
                new_priority = input("Enter new Priority (High/Medium/Low): ")
                tasks[task_index]["task"] = new_task_name
                tasks[task_index]["priority"] = new_priority
                print("Task updated successfully.")
            else:
                print("Invalid task number.")

        except ValueError:
            print("Invalid input. Please enter a valid task number.")


def delete_task():
    if not tasks:
        print("No task to Delete.")
    else:
        view_tasks()
        try:
            task_index = int(input("Enter the task number: ")) - 1

            if 0 <= task_index < len(tasks):
                tasks.pop(task_index)
                print("Task deleted successfully.")
            else:
                print("Invalid task number.")

        except ValueError:
            print("Invalid input. Please enter a valid task number.")


def task_completed():
    if not tasks:
        print("No task to mark as completed.")
    else:
        view_tasks()
        try:
            task_index = int(input("Enter the task number to mark as completed: ")) - 1

            if 0 <= task_index < len(tasks):
                tasks[task_index]["status"] = "completed"
                print(f"Task '{tasks[task_index]['task']}' marked as completed.")
            else:
                print("Invalid task number.")

        except ValueError:
            print("Invalid input. Please enter a valid task number.")


def main():
    load_tasks()
    print("===Welcome to CloudTask Management===")
    print("--CloudTask: --")

    while True:
        print("\n---Task Management Menu---")
        print("1. Add Task")
        print("2. View Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Completed")
        print("6. Save Tasks to JSON");
        print("7. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == "1":
            task_name = input("Enter Task: ")
            priority = input("Enter Priority (High/Medium/Low): ")
            add_task(task_name, priority)

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            update_task()

        elif choice == "4":
            delete_task()

        elif choice == "5":
            task_completed()

        elif choice == "6":
            save_tasks()

        elif choice == "7":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()