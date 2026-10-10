from .viewTask import viewTask
def updateTask(tasks):
    if not tasks:
        print("no task to update");
        return;
    else:
        viewTask(tasks);
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