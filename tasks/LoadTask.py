import json
def loadTasks():
    global tasks;
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        print("No existing tasks found. Starting with an empty task list.")

    return tasks;