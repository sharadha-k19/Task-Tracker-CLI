# Task Tracker CLI

A simple command-line interface (CLI) application to track and manage tasks. This project allows users to add, update, delete, and organize tasks by status using a JSON file for persistence.

This project is beginner-friendly and demonstrates working with the filesystem, command-line arguments, and basic data handling without using any external libraries.

---

## 🚀 Features

* Add new tasks
* Update existing tasks
* Delete tasks
* Mark tasks as **todo**, **in-progress**, or **done**
* List all tasks
* List tasks by status (todo / in-progress / done)
* Persistent storage using a JSON file
* Graceful handling of edge cases

---

## 🛠 Tech Stack

* **Language:** Python 3
* **Libraries:** Built-in Python modules only (`sys`, `json`, `os`, `datetime`)
* **Storage:** JSON file

---

## 📂 Project Structure

```
task-tracker/
│
├── task_cli.py      # Main CLI application
└── tasks.json       # Auto-generated task storage file
```

---

## ⚙️ Installation & Setup

### Prerequisites

* Python 3 installed

Check installation:

```bash
python3 --version
```

### Clone the Repository

```bash
git clone https://github.com/<your-username>/task-tracker-cli.git
cd task-tracker-cli
```

---

## ▶️ Usage

Run all commands using `python3`:

### Add a Task

```bash
python3 task_cli.py add "Buy groceries"
```

### Update a Task

```bash
python3 task_cli.py update 1 "Buy groceries and cook dinner"
```

### Delete a Task

```bash
python3 task_cli.py delete 1
```

### Mark Task Status

```bash
python3 task_cli.py mark-in-progress 1
python3 task_cli.py mark-done 1
```

### List Tasks

```bash
python3 task_cli.py list
python3 task_cli.py list todo
python3 task_cli.py list in-progress
python3 task_cli.py list done
```

---

## 🧾 Task Properties

Each task stored in `tasks.json` contains:

* `id` – Unique task identifier
* `description` – Short task description
* `status` – todo / in-progress / done
* `createdAt` – Timestamp when task was created
* `updatedAt` – Timestamp of last update

Example:

```json
{
  "id": 1,
  "description": "Learn Task Tracker CLI",
  "status": "todo",
  "createdAt": "2026-01-21 18:55:10",
  "updatedAt": "2026-01-21 18:55:10"
}
```

---

## 🧠 Learning Outcomes

* Command-line argument handling
* File read/write operations
* JSON-based data persistence
* Error handling and validation
* Building real-world CLI tools

---

## 🌱 Future Enhancements

* Task priorities
* Due dates
* Search functionality
* Convert to executable (`task-cli`)
* Unit testing

---

## 👩‍💻 Author

🙋‍♀️ Author Sharadha Kattalingannagari 📧 sharadhakattalingannagari@gmail.com 🔗 LinkedIn : https://www.linkedin.com/in/sharadha-kattalingannagari-992a4730a

---
https://roadmap.sh/projects/task-tracker

## 📄 License

This project is open-source and free to use for learning purposes.



## 🔗 Project Repository
https://github.com/sharadha-k19/Task-Tracker-CLI

