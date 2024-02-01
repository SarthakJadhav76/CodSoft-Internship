import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entrytask.get()
    if task:
        listbox.insert(tk.END, task)
        entrytask.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning!", "No Task Is Entered")

def delete_task():
    try:
        task_index = listbox.curselection()[0]
        listbox.delete(task_index)
    except IndexError:
        messagebox.showwarning("Warning!", "No Task Is Selected")

def edit_task():
    try:
        task_index = listbox.curselection()[0]
        previous_task_name = listbox.get(task_index)
        task = entrytask.get()
        if task and previous_task_name != task:
            listbox.delete(task_index)
            listbox.insert(task_index, task)
            entrytask.delete(0, tk.END)
            messagebox.showinfo("Successfully edited", "😃")
        elif previous_task_name == task:
            entrytask.delete(0, tk.END)
            messagebox.showwarning("Name is Same", "Previous And Present Names Are The Same")
        else:
            messagebox.showwarning("Warning!", "The Task Name Can't Be Empty")
    except IndexError:
        messagebox.showwarning("Warning!", "Nothing Is Selected!!")

m = tk.Tk()
m.title("To-Do List")

m.geometry("400x400")
m.configure(bg="#F0F0F0")

frame_tasks = tk.Frame(m, bg="#F0F0F0")
frame_tasks.pack(pady=10)

listbox = tk.Listbox(frame_tasks, height=10, width=30, selectbackground="#FFE4B5", selectforeground="black", font=("Arial", 12))
listbox.pack(side=tk.LEFT, ipady=10)

scrollbar = tk.Scrollbar(frame_tasks, orient=tk.VERTICAL, command=listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.config(yscrollcommand=scrollbar.set)

entrytask = tk.Entry(m, width=30, font=("Arial", 12))
entrytask.pack(pady=10)

buttons = [
    ("Add Task", add_task, "#B0FC38"),
    ("Delete Task", delete_task, "#ff0000"),
    ("Edit Task", edit_task, "#0000ff")
]

for btn_text, btn_command, btn_bg in buttons:
    button = tk.Button(m, text=btn_text, width=30, command=btn_command, bg=btn_bg, fg="black", font=("Arial", 12))
    button.pack()

m.mainloop()
