import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from tkcalendar import Calendar
import json
import os
from datetime import datetime

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.filename = 'todo_list.json'
        self.tasks = self.load_tasks()

        # Create UI components
        self.create_widgets()
        self.update_task_listbox()

    def create_widgets(self):
        # Task Entry
        self.task_entry = tk.Entry(self.root, width=40, font=("Helvetica", 12))
        self.task_entry.pack(pady=10)

        # Calendar for Due Date
        self.calendar_label = tk.Label(self.root, text="Select Due Date:", font=("Helvetica", 12), bg="#f0f0f0")
        self.calendar_label.pack(pady=5)
        self.calendar = Calendar(self.root, selectmode='day', year=2023, month=10, day=1)
        self.calendar.pack(pady=10)

        # Add Task Button
        self.add_task_button = tk.Button(self.root, text="Add Task", command=self.add_task, font=("Helvetica", 12), bg="#4CAF50", fg="white")
        self.add_task_button.pack(pady=10)

        # Task Listbox with Scrollbar
        self.task_frame = tk.Frame(self.root)
        self.task_frame.pack(pady=10)

        self.task_listbox = tk.Listbox(self.task_frame, width=60, height=15, font=("Helvetica", 12), bg="#ADD8E6")
        self.task_listbox.pack(side=tk.LEFT)

        self.scrollbar = tk.Scrollbar(self.task_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        # Complete Task Button
        self.complete_task_button = tk.Button(self.root, text="Complete Task", command=self.complete_task, font=("Helvetica", 12), bg="#2196F3", fg="white")
        self.complete_task_button.pack(pady=5)

        # Delete Task Button
        self.delete_task_button = tk.Button(self.root, text="Delete Task", command=self.delete_task, font=("Helvetica", 12), bg="#f44336", fg="white")
        self.delete_task_button.pack(pady=5)

        # Show Completed Tasks Button
        self.show_completed_button = tk.Button(self.root, text="Show Completed Tasks", command=self.show_completed_tasks, font=("Helvetica", 12), bg="#FFC107", fg="black")
        self.show_completed_button.pack(pady=5)

        # Show Pending Tasks Button
        self.show_pending_button = tk.Button(self.root, text="Show Pending Tasks", command=self.show_pending_tasks, font=("Helvetica", 12), bg="#FF9800", fg="black")
        self.show_pending_button.pack(pady=5)

        # Show Upcoming Tasks Button
        self.show_upcoming_button = tk.Button(self.root, text="Show Upcoming Tasks", command=self.show_upcoming_tasks, font=("Helvetica", 12), bg="#9C27B0", fg="white")
        self.show_upcoming_button.pack(pady=5)

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file)

    def add_task(self):
        task = self.task_entry.get()
        due_date = self.calendar.get_date()

        if task and due_date:
            self.tasks.append({'task': task, 'due_date': due_date, 'completed': False})
            self.save_tasks()
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please fill in all fields.")

    def complete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.tasks[selected_index]['completed'] = True
            self.save_tasks()
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to complete.")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.tasks.pop(selected_index)
            self.save_tasks()
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "✓" if task['completed'] else "✗"
            color = "green" if task['completed'] else "red"
            self.task_listbox.insert(tk.END, f"[{status}] {task['task']} (Due: {task['due_date']})")
            self.task_listbox.itemconfig(tk.END, {'fg': color})

    def show_completed_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            if task['completed']:
                self.task_listbox.insert(tk.END, f"[✓] {task['task']} (Due: {task['due_date']})")
                self.task_listbox.itemconfig(tk.END, {'fg': 'green'})

    def show_pending_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            if not task['completed']:
                self.task_listbox.insert(tk.END, f"[✗] {task['task']} (Due: {task['due_date']})")
                self.task_listbox.itemconfig(tk.END, {'fg': 'red'})

    def show_upcoming_tasks(self):
        today = datetime.now().date()
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            due_date = datetime.strptime(task['due_date'], "%Y-%m-%d").date()
            if not task['completed'] and due_date >= today:
                self.task_listbox.insert(tk.END, f"[✗] {task['task']} (Due: {task['due_date']})")
                self.task_listbox.itemconfig(tk.END, {'fg': 'red'})

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()