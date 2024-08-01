import tkinter as tk
from tkinter import ttk
import threading
import time

# Create the main window
root = tk.Tk()
root.geometry('400x300')
root.title('Multithreading Tkinter Demo')

# Define a long-running task
def long_running_task(label):
    for i in range(10):
        time.sleep(1)  # Simulate a time-consuming task
        label.config(text=f"Task running... {i+1}/10")
    label.config(text="Task completed!")

# Start the task in a separate thread
def start_task(label):
    thread = threading.Thread(target=long_running_task, args=(label,))
    thread.start()

# Create a label to display the task status
status_label = ttk.Label(root, text="Click the button to start the task")
status_label.pack(pady=20)

# Create a button to start the task
start_button = ttk.Button(root, text="Start Task", command=lambda: start_task(status_label))
start_button.pack(pady=10)

# Run the application
root.mainloop()