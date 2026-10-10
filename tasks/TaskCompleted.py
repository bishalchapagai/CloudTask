from .viewTask import viewTask

def task_completed(tasks):
    if not tasks:
        print("No task to mark as completed.")
    else:
        viewTask(tasks)
        try:
            task_index = int(input("Enter the task number to mark as completed: ")) - 1

            if 0 <= task_index < len(tasks):
                tasks[task_index]["status"] = "completed"
                print(f"Task '{tasks[task_index]['task']}' marked as completed.")
            else:
                print("Invalid task number.")

        except ValueError:
            print("Invalid input. Please enter a valid task number.")