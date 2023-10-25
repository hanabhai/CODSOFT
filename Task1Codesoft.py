  import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        task_list.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Also Enter Here.")

def delete_task():
    try:
        selected_task = task_list.get(task_list.curselection())
        task_list.delete(tk.ACTIVE)
    except:
        messagebox.showwarning("Warning", "Select Task")

def update_task():
    try:
        selected_task = task_list.get(task_list.curselection())
        entry.delete(0, tk.END)
        entry.insert(0, selected_task)
        delete_task()
    except:
        messagebox.showwarning("Warning", "Select Update Task")

app = tk.Tk()
app.title("To-Do List")

frame = tk.Frame(app)
frame.pack(pady=10)

task_list = tk.Listbox(frame, height=10, width=50)
task_list.pack(side=tk.LEFT)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

task_list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_list.yview)

entry = tk.Entry(app, width=40)
entry.pack()

add_button = tk.Button(app, text="Add Task", width=40, command=add_task)
add_button.pack()

delete_button = tk.Button(app, text="Delete Task", width=40, command=delete_task)
delete_button.pack()

update_button = tk.Button(app, text="Update Task", width=40, command=update_task)
update_button.pack()

app.mainloop()
