✅ To-Do List Desktop App
📌 Project Overview

This project is a To-Do List Desktop Application built in Python to demonstrate Object-Oriented Programming (OOP) principles.
The app allows users to:

Create and manage daily tasks

Organize tasks by categories

Mark tasks as completed or pending

Delete tasks when finished

The project highlights OOP design patterns by using classes for tasks, task lists, and the main application logic.

🎯 OOP Concepts Demonstrated

Encapsulation – Each task is represented as a Task object with its own properties (title, description, status).

Abstraction – Task management (add, update, delete, complete) is handled through clean class methods.

Inheritance – Can be extended with specialized task types (e.g., WorkTask, PersonalTask).

Polymorphism – Different task objects can be displayed and managed through a common interface.

⚙️ Features

✅ Add new tasks with title and description

✅ Edit existing tasks

✅ Mark tasks as completed

✅ Delete tasks

✅ Display task list with status

✅ Persistent storage (optional: file/SQLite database)

🛠️ Tech Stack

Python (OOP implementation)

Tkinter / PyQt (for GUI – depending on your implementation)

SQLite / JSON (for storing tasks – optional)

📂 Project Structure
📦 ToDo-App
 ┣ 📜 main.py             # Entry point for the app
 ┣ 📜 task.py             # Task class (encapsulation of task details)
 ┣ 📜 task_manager.py     # Handles task operations (add, delete, complete)
 ┣ 📜 ui.py               # GUI logic (Tkinter/PyQt)
 ┣ 📜 tasks.db/json       # (Optional) Database/file for saving tasks
 ┣ 📜 README.md           # Project documentation

🚀 How to Run

Clone the repository:

git clone https://github.com/your-username/ToDo-App.git
cd ToDo-App


Install dependencies (if using Tkinter, no extra install needed; for PyQt, install via pip):

pip install pyqt5


Run the app:

python main.py

📸 Demo

Add a screenshot or GIF of your app UI here.

🎓 Academic Context

This project was built as part of an Object-Oriented Programming course project, with the following goals:

To implement OOP principles in Python.

To create a real-world desktop application.

To demonstrate clean design and modularity with classes.
