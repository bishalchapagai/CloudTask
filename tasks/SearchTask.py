def searchTask(tasks):
    if not tasks:
        print("No task to search.")
        return

    search = input("Enter task name: ").strip().lower()

    if not search:
        print("Search cannot be empty.")
        return

    found = False

    for task in tasks:
        if search in task["task"].lower():
            print(
                f"Task: {task['task']} / "
                f"Priority: {task['priority']} / "
                f"Status: {task['status']}"
            )
            found = True

    if not found:
        print("Task not found.")