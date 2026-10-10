import json;
from tasks import addTask,updateTask,viewTask,loadTasks,searchTask,saveTasks,deleteTask;



tasks = [];
def load_tasks():
    global tasks;
    tasks = loadTasks();


def search_task():
    searchTask(tasks);

#view tasks
def view_tasks(tasks):
     viewTask(tasks);
    

def delete_task():
    deleteTask(tasks);

def task_completed():
    task_completed(tasks);

def save_tasks():
    saveTasks(tasks);

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
        print("7. search")
        print("8. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == "1":
            addTask(tasks);

        elif choice == "2":
            view_tasks(tasks);

        elif choice == "3":
            updateTask(tasks);

        elif choice == "4":
            delete_task()

        elif choice == "5":
            task_completed()

        elif choice == "6":
            save_tasks()
        elif choice == "7":
            search_task()
        elif choice == "8":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()