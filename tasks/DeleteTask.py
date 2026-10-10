from .viewTask import viewTask
def deleteTask(tasks):
    if not tasks:
        print("No task to Delete.")
    else:
        viewTask(tasks)
        try:
            task_index = int(input("Enter the task number: ")) - 1

            if 0 <= task_index < len(tasks):
                tasks.pop(task_index)
                print("Task deleted successfully.")
            else:
                print("Invalid task number.")

        except ValueError:
            print("Invalid input. Please enter a valid task number.")
