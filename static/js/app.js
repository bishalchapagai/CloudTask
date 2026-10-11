
let tasks = [];

// Access HTML elements
const taskForm = document.getElementById("taskForm");
const taskName = document.getElementById("taskName");
const priority = document.getElementById("priority");
const taskList = document.getElementById("taskList");

const totalTasks = document.getElementById("totalTasks");
const pendingTasks = document.getElementById("pendingTasks");
const completedTasks = document.getElementById("completedTasks");


// LOAD TASKS FROM FLASK
async function loadTasks() {
    try {
        const response = await fetch("/api/tasks");

        if (!response.ok) {
            throw new Error("Failed to load tasks");
        }

        tasks = await response.json();
        displayTasks();

    } catch (error) {
        console.error(error);
        alert("Could not load tasks from Flask.");
    }
}


// ADD TASK
async function addTask(name, taskPriority) {
    try {
        const response = await fetch("/api/tasks", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                task: name,
                priority: taskPriority
            })
        });

        if (!response.ok) {
            throw new Error("Failed to add task");
        }

        await loadTasks();

    } catch (error) {
        console.error(error);
        alert("Could not save task.");
    }
}


// DISPLAY TASKS
function displayTasks() {
    taskList.innerHTML = "";

    if (tasks.length === 0) {
        const message = document.createElement("p");
        message.className = "empty-message";
        message.textContent = "No tasks available.";
        taskList.appendChild(message);
    }

    tasks.forEach((task) => {
        const div = document.createElement("div");
        div.className = "task-item";

        if (task.status === "completed") {
            div.classList.add("completed");
        }

        const details = document.createElement("div");
        details.className = "task-info";

        const title = document.createElement("h3");
        title.textContent = task.task;

        const info = document.createElement("p");
        info.textContent =
            `Priority: ${task.priority} | Status: ${task.status}`;

        details.appendChild(title);
        details.appendChild(info);

        const actions = document.createElement("div");
        actions.className = "task-actions";

        const completeButton = document.createElement("button");
        completeButton.className = "complete-btn";
        completeButton.textContent = "Complete";
        completeButton.disabled = task.status === "completed";

        completeButton.addEventListener("click", () => {
            completeTask(task.id);
        });

        const deleteButton = document.createElement("button");
        deleteButton.className = "delete-btn";
        deleteButton.textContent = "Delete";

        deleteButton.addEventListener("click", () => {
            deleteTask(task.id);
        });

        actions.appendChild(completeButton);
        actions.appendChild(deleteButton);

        div.appendChild(details);
        div.appendChild(actions);

        taskList.appendChild(div);
    });

    updateStats();
}


// COMPLETE TASK
async function completeTask(id) {
    try {
        const response = await fetch(`/api/tasks/${id}`, {
            method: "PATCH"
        });

        if (!response.ok) {
            throw new Error("Failed to complete task");
        }

        await loadTasks();

    } catch (error) {
        console.error(error);
        alert("Could not complete task.");
    }
}


// DELETE TASK
async function deleteTask(id) {
    try {
        const response = await fetch(`/api/tasks/${id}`, {
            method: "DELETE"
        });

        if (!response.ok) {
            throw new Error("Failed to delete task");
        }

        await loadTasks();

    } catch (error) {
        console.error(error);
        alert("Could not delete task.");
    }
}


// UPDATE DASHBOARD
function updateStats() {
    totalTasks.textContent = tasks.length;

    pendingTasks.textContent = tasks.filter(
        task => task.status === "incomplete"
    ).length;

    completedTasks.textContent = tasks.filter(
        task => task.status === "completed"
    ).length;
}


// FORM SUBMISSION
taskForm.addEventListener("submit", async function(event) {
    event.preventDefault();

    const name = taskName.value.trim();
    const selectedPriority = priority.value;

    if (name === "") {
        alert("Task name cannot be empty.");
        return;
    }

    await addTask(name, selectedPriority);

    taskForm.reset();
});


// LOAD SAVED TASKS WHEN PAGE OPENS
loadTasks();
