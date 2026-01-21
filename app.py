from flask import Flask, request, redirect, url_for, render_template_string
import json
import os
from datetime import datetime

app = Flask(__name__)
FILE_NAME = "tasks.json"

# ---------- Utility Functions ----------

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        return json.load(f)


def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)


def timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# ---------- Routes ----------

@app.route("/", methods=["GET", "POST"])
def index():
    tasks = load_tasks()

    if request.method == "POST":
        description = request.form.get("description")
        if description:
            task_id = tasks[-1]["id"] + 1 if tasks else 1
            tasks.append({
                "id": task_id,
                "description": description,
                "status": "todo",
                "createdAt": timestamp(),
                "updatedAt": timestamp()
            })
            save_tasks(tasks)
        return redirect(url_for("index"))

    return render_template_string(TEMPLATE, tasks=tasks)


@app.route("/update/<int:task_id>/<status>")
def update_status(task_id, status):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            task["updatedAt"] = timestamp()
            break
    save_tasks(tasks)
    return redirect(url_for("index"))


@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    tasks = load_tasks()
    tasks = [t for t in tasks if t["id"] != task_id]
    save_tasks(tasks)
    return redirect(url_for("index"))

# ---------- HTML Template ----------

TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Task Tracker</title>
    <style>
        body { font-family: Arial; margin: 40px; }
        h1 { color: #333; }
        form { margin-bottom: 20px; }
        input { padding: 8px; width: 300px; }
        button { padding: 8px 12px; }
        table { width: 100%; border-collapse: collapse; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: center; }
        th { background-color: #f4f4f4; }
        a { margin: 0 5px; }
    </style>
</head>
<body>
    <h1>Task Tracker</h1>

    <form method="post">
        <input type="text" name="description" placeholder="Enter new task" required />
        <button type="submit">Add Task</button>
    </form>

    <table>
        <tr>
            <th>ID</th>
            <th>Description</th>
            <th>Status</th>
            <th>Actions</th>
        </tr>
        {% for task in tasks %}
        <tr>
            <td>{{ task.id }}</td>
            <td>{{ task.description }}</td>
            <td>{{ task.status }}</td>
            <td>
                <a href="/update/{{ task.id }}/in-progress">In Progress</a>
                <a href="/update/{{ task.id }}/done">Done</a>
                <a href="/delete/{{ task.id }}">Delete</a>
            </td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(debug=True)
