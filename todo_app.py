import tkinter as tk
from tkinter import simpledialog, messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = []

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        self.task_listbox = tk.Listbox(
            self.frame, width=50, height=10, font="Arial 14"
        )
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        self.entry_frame = tk.Frame(self.root)
        self.entry_frame.pack(pady=10)

        self.task_entry = tk.Entry(
            self.entry_frame, font="Arial 14", width=38
        )
        self.task_entry.pack(side=tk.LEFT, padx=10)

        self.add_button = tk.Button(
            self.entry_frame, text="Add Task", font="Arial 14", command=self.add_task
        )
        self.add_button.pack(side=tk.LEFT)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=20)

        self.edit_button = tk.Button(
            self.button_frame, text="Edit Task", font="Arial 14", command=self.edit_task
        )
        self.edit_button.pack(side=tk.LEFT, padx=10)

        self.delete_button = tk.Button(
            self.button_frame, text="Delete Task", font="Arial 14", command=self.delete_task
        )
        self.delete_button.pack(side=tk.LEFT, padx=10)

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def edit_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            new_task = simpledialog.askstring("Edit Task", "Edit the task:", initialvalue=self.tasks[selected_task_index[0]])
            if new_task:
                self.tasks[selected_task_index[0]] = new_task
                self.update_task_listbox()
        else:
            messagebox.showwarning("Warning", "You must select a task to edit.")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            del self.tasks[selected_task_index[0]]
            self.update_task_listbox()
        else:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
