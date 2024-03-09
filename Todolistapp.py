import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

root = tk.Tk()
root.title("To-Do List App")

# Create frames
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

tasks_frame = tk.Frame(root)
tasks_frame.pack(padx=10, pady=5)

# Task entry
task_entry = tk.Entry(input_frame, width=40)
task_entry.pack(side=tk.LEFT, padx=5)

add_button = tk.Button(input_frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT)

# Task list
tasks_listbox = tk.Listbox(tasks_frame, width=50)
tasks_listbox.pack(side=tk.LEFT)

scrollbar = tk.Scrollbar(tasks_frame, orient=tk.VERTICAL)
scrollbar.config(command=tasks_listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

tasks_listbox.config(yscrollcommand=scrollbar.set)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

root.mainloop()
