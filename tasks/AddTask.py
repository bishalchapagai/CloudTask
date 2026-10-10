def addTask(tasks):
    task = input("Enter the task we want to add: ").strip()
    priority = input("Enter priority (High/Medium/Low): ").strip()

    tasks.append({
        "task": task,
        "priority": priority,
        "status": "pending"
    })

    print("Task added successfully.")