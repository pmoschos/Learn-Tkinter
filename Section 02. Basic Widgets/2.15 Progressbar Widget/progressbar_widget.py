import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Progressbar Widget Example")
root.geometry("300x100")

# Create and pack a Progressbar widget
progressbar = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
progressbar.pack(pady=20)

# Function to start the progressbar
def start_progress():
    progressbar.start(10)  # Increment every 10ms

# Function to stop the progressbar
def stop_progress():
    progressbar.stop()

# Create and pack Buttons to start and stop the progressbar
start_button = ttk.Button(root, text="Start", command=start_progress)
start_button.pack(side="left", padx=10)

stop_button = ttk.Button(root, text="Stop", command=stop_progress)
stop_button.pack(side="right", padx=10)

# Run the application
root.mainloop()