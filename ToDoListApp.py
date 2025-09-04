# Applying All 4 OOP Encapsulation, Abstraction, Polymorphism, and Inheritance
from abc import ABC, abstractmethod
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import os

# Abstract class to define the task manager interface
class AbstractTaskManager(ABC):
    @abstractmethod
    def add_task(self, task):
        pass

    @abstractmethod
    def delete_task(self, task):
        pass

    @abstractmethod
    def load_tasks(self):
        pass
# Base class to demonstrate polymorphism and inheritance
class BaseTaskManager:
    def __init__(self):
        self.task_list = []

    def add_task(self, task):
        print("Adding task in base class")
        self.task_list.append(task)

    def delete_task(self, task):
        print("Deleting task in base class")
        if task in self.task_list:
            self.task_list.remove(task)


# Derived class that overrides behavior (Inheritance + Polymorphism)
class TaskManager(BaseTaskManager):
    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path
        self.load_tasks()

    def add_task(self, task):
        if task:
            print("Adding task in file-based manager")
            self.task_list.append(task)
            self.save_tasks()

    def delete_task(self, task):
        print("Deleting task in file-based manager")
        if task in self.task_list:
            self.task_list.remove(task)
            self.save_tasks()

    def load_tasks(self):
        if not os.path.exists(self.file_path):
            os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
            open(self.file_path, 'w').close()

        with open(self.file_path, 'r') as file:
            self.task_list = [task.strip() for task in file.readlines() if task.strip()]

    def save_tasks(self):
        with open(self.file_path, 'w') as file:
            for task in self.task_list:
                file.write(f"{task}\n")


# To-Do List UI
class ToDoList(Tk):
    def __init__(self):
        super().__init__()
        self.title("To Do List App")
        self.geometry("400x650")
        self.resizable(False, False)
        self.manager = TaskManager("D:/py.github/tkinter learning/ToDoList/tasklist.txt")

        self.setup_ui()
        self.load_tasks_to_listbox()

    def setup_ui(self):
        # Adding icon
        ic_img = Image.open(r"D:\py.github\tkinter learning\ToDoList\images\task.png")
        self.icon_image = ImageTk.PhotoImage(ic_img)
        self.iconphoto(True, self.icon_image)

        # Bar
        top_img = Image.open(r"D:\py.github\tkinter learning\ToDoList\images\topbar.png")
        self.TopImage = ImageTk.PhotoImage(top_img)
        lbl_top = Label(self, image=self.TopImage)
        lbl_top.pack()

        # Dock image
        d_img = Image.open(r"D:\py.github\tkinter learning\ToDoList\images\dock.png")
        self.dock_image = ImageTk.PhotoImage(d_img)
        lbl_dock = Label(self, image=self.dock_image, bg="#32405b")
        lbl_dock.place(x=30, y=25)

        # Notes image
        notes = Image.open(r"D:\py.github\tkinter learning\ToDoList\images\task.png")
        self.note_image = ImageTk.PhotoImage(notes)
        lbl_notes = Label(self, image=self.note_image, bg="#32405b")
        lbl_notes.place(x=340, y=25)

        head = Label(self, text="All Task", font=("family", 20, "bold"), fg="white", bg="#32405b")
        head.place(x=130, y=20)

        # Frame
        frame = Frame(self, width=400, height=50, bg="white")
        frame.place(x=0, y=150)

        # Entry
        self.task_entry = Entry(frame, width=18, font=("arial", 20), bd=0)
        self.task_entry.place(x=0, y=7)
        self.task_entry.focus()

        # Button
        self.button = Button(frame, text="Add", font=("arial", 20, "bold"), width=6,
                             bg="#32405b", fg="#fff", bd=0, command=self.Add_task)
        self.button.place(x=300, y=0)

        # ListBox
        frame_ = Frame(self, bd=3, width=700, height=250, bg="#32405b")
        frame_.pack(pady=(160, 0))

        self.listbox = Listbox(frame_, font=("arial", 12), width=40, height=16,
                               bg="#32405b", fg="white", cursor="hand2", selectbackground="#5a95ff")
        self.listbox.pack(side=LEFT, fill=BOTH, padx=2)

        scroll = Scrollbar(frame_)
        scroll.pack(side=RIGHT, fill=BOTH)
        self.listbox.config(yscrollcommand=scroll.set)
        scroll.config(command=self.listbox.yview)

        # Delete button
        del_ic = Image.open(r"D:\py.github\tkinter learning\ToDoList\images\delete.png")
        self.delete_icon = ImageTk.PhotoImage(del_ic)
        Button(self, image=self.delete_icon, bd=0, command=self.delete_task).pack(side=BOTTOM, pady=13)

    def Add_task(self):
        task = self.task_entry.get()
        self.task_entry.delete(0, END)
        if task:
            self.manager.add_task(task)
            self.listbox.insert(END, task)

    def delete_task(self):
        task = str(self.listbox.get(ANCHOR))
        if task:
            self.manager.delete_task(task)
            self.listbox.delete(ANCHOR)

    def load_tasks_to_listbox(self):
        for task in self.manager.task_list:
            self.listbox.insert(END, task)


if __name__ == "__main__":
    app = ToDoList()
    app.mainloop()