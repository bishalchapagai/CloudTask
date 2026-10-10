import json
def saveTasks(tasks):

    with open("tasks.json","w") as file:
        json.dump(tasks,file,indent =4);