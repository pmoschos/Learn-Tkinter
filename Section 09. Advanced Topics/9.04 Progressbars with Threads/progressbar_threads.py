import tkinter as tk
from tkinter import ttk
import threading
import time

# Create the main window
root = tk.Tk()
root.geometry('400x200')
root.title('Progressbar with Threads Demo')

# Create a progress bar
progress = ttk.Progressbar(root, orient='horizontal', mode='determinate', length=300)
progress.pack(pady=20)

# Define a long-running task
def long_running_task():
    for i in range(100):
        time.sleep(0.1)  # Simulate a time-consuming task
        progress['value'] = i + 1
    progress['value'] = 100

# Start the task in a separate thread
def start_task():
    thread = threading.Thread(target=long_running_task)
    thread.start()

# Create a button to start the task
start_button = ttk.Button(root, text='Start Task', command=start_task)
start_button.pack(pady=10)

# Run the application
root.mainloop()