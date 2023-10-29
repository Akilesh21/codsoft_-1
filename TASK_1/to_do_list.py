# Task 1 TO-DO-LIST ---{CODSOFT}
import tkinter as tk

def add_task():
    task = enter_task .get()
    if task:
        task_list.insert(tk.END, task)
        enter_task .delete(0, tk.END)

def remove_task():
    selected_task_index = task_list.curselection()
    if selected_task_index:
        task_list.delete(selected_task_index)

def clear_completed():
    task_list.delete(0, tk.END)

def prioritize_task():
    selected_task_index = task_list.curselection()
    if selected_task_index:
        task = task_list.get(selected_task_index)
        task_list.delete(selected_task_index)
        task_list.insert(tk.END, f"⭐ {task}")
# Create the main application window
app = tk.Tk()
app.title("To-Do List")
# Task entry field
enter_task = tk.Entry(app, width=30)
enter_task.grid(row=0, column=0, padx=10, pady=10, columnspan=3)
# Add Task button
add = tk.Button(app, text="Add Task", command=add_task)
add.grid(row=0, column=3, padx=10, pady=10)
# Task listbox
task_list = tk.Listbox(app, selectmode=tk.SINGLE, width=40, height=10)
task_list.grid(row=1, column=0, columnspan=4, padx=10, pady=10)
# Remove Task button
remove = tk.Button(app, text="Remove Task", command=remove_task)
remove.grid(row=2, column=0, padx=10, pady=10)
# Clear Completed button
clear = tk.Button(app, text="Clear Completed", command=clear_completed)
clear.grid(row=2, column=1, padx=10, pady=10)
# Prioritize Task button
prioritize = tk.Button(app, text="Prioritize Task", command=prioritize_task)
prioritize.grid(row=2, column=2, padx=10, pady=10)
app.mainloop()
