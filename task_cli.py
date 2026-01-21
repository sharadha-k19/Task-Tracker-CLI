import sys
import json
import os
from datetime import datetime

FILE_NAME = "tasks.json"


def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        return json.load(f)


def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)


def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def add_task(description):
    tasks = load_tasks()
    task_id = tasks[-1]["id"] + 1 if tasks else 1

    task = {
        "id": task_id,
        "description": description,
        "status": "todo",
        "createdAt": get_timestamp(),
        "updatedAt": get_timestamp(),
    }

    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {task_id})")


def update_task(task_id, description):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = description
            task["updatedAt"] = get_timestamp()
            save_tasks(tasks)
            print("Task updated successfully")
            return
    print("Task not found")


def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = [task for task in tasks if task["id"] != task_id]

    if len(new_tasks) == len(tasks):
        print("Task not found")
        return

    save_tasks(new_tasks)
    print("Task deleted successfully")


def mark_task(task_id, status):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            task["updatedAt"] = get_timestamp()
            save_tasks(tasks)
            print(f"Task marked as {status}")
            return
    print("Task not found")


def list_tasks(filter_status=None):
    tasks = load_tasks()

    if filter_status:
        tasks = [t for t in tasks if t["status"] == filter_status]

    if not tasks:
        print("No tasks found")
        return

    for task in tasks:
        print(
            f"[{task['id']}] {task['description']} "
            f"({task['status']}) | Created: {task['createdAt']}"
        )


def main():
    if len(sys.argv) < 2:
        print("Usage: task-cli <command> [arguments]")
        return

    command = sys.argv[1]

    if command == "add":
        add_task(sys.argv[2])

    elif command == "update":
        update_task(int(sys.argv[2]), sys.argv[3])

    elif command == "delete":
        delete_task(int(sys.argv[2]))

    elif command == "mark-in-progress":
        mark_task(int(sys.argv[2]), "in-progress")

    elif command == "mark-done":
        mark_task(int(sys.argv[2]), "done")

    elif command == "list":
        if len(sys.argv) == 3:
            list_tasks(sys.argv[2])
        else:
            list_tasks()

    else:
        print("Unknown command")


if __name__ == "__main__":
    main()
