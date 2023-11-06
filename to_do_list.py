import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    selected_task = listbox.curselection()
    if selected_task:
        index = selected_task[0]
        listbox.delete(index)
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create a listbox to display tasks
listbox = tk.Listbox(root, selectmode=tk.SINGLE)
listbox.pack(pady=10)

# Create an entry widget to add new tasks
entry = tk.Entry(root)
entry.pack(pady=10)

# Create Add and Delete buttons
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack()

# Run the application
root.mainloop()
