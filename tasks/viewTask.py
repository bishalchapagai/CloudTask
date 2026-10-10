def viewTask(tasks):
    if not tasks:
        print("no task to view.")
    else:
        for index,t in enumerate(tasks,start=1):
            print(f"{index}. Task: {t['task']} / priority: {t['priority']} / status: {t['status']}")
