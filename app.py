
import json
from pathlib import Path
from uuid import uuid4

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

DATA_FILE = Path(__file__).resolve().parent / "tasks.json"


# READ TASKS FROM JSON
def load_tasks():
    if not DATA_FILE.exists():
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        tasks = json.load(file)

    if not isinstance(tasks, list):
        raise ValueError("tasks.json must contain a list")

    # Support tasks created by our earlier CLI program
    changed = False

    for task in tasks:
        if not isinstance(task, dict):
            raise ValueError("Each task must be a JSON object")

        if "id" not in task:
            task["id"] = str(uuid4())
            changed = True

        if "status" not in task:
            task["status"] = "incomplete"
            changed = True

    if changed:
        save_tasks(tasks)

    return tasks


# SAVE TASKS TO JSON
def save_tasks(tasks):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)


# HOMEPAGE
@app.route("/")
def home():
    return render_template("index.html")


# GET ALL TASKS
@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    tasks = load_tasks()
    return jsonify(tasks)


# ADD A TASK
@app.route("/api/tasks", methods=["POST"])
def add_task():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON data"}), 400

    name = data.get("task", "")
    priority = data.get("priority", "Medium")

    if not isinstance(name, str) or not name.strip():
        return jsonify({"error": "Task name is required"}), 400

    if priority not in ("High", "Medium", "Low"):
        return jsonify({"error": "Invalid priority"}), 400

    tasks = load_tasks()

    new_task = {
        "id": str(uuid4()),
        "task": name.strip(),
        "priority": priority,
        "status": "incomplete"
    }

    tasks.append(new_task)
    save_tasks(tasks)

    return jsonify(new_task), 201


# COMPLETE A TASK
@app.route("/api/tasks/<task_id>", methods=["PATCH"])
def complete_task(task_id):
    tasks = load_tasks()

    for task in tasks:
        if str(task["id"]) == task_id:
            task["status"] = "completed"
            save_tasks(tasks)
            return jsonify(task)

    return jsonify({"error": "Task not found"}), 404


# DELETE A TASK
@app.route("/api/tasks/<task_id>", methods=["DELETE"])
def delete_task(task_id):
    tasks = load_tasks()

    remaining = [
        task for task in tasks
        if str(task["id"]) != task_id
    ]

    if len(remaining) == len(tasks):
        return jsonify({"error": "Task not found"}), 404

    save_tasks(remaining)

    return jsonify({"message": "Task deleted successfully"})


if __name__ == "__main__":
    app.run(debug=True)
