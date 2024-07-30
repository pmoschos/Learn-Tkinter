import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Frame Widget Example")

# Create and pack a Frame widget
frame = ttk.Frame(root, padding="10")
frame.pack(padx=10, pady=10, fill='x', expand=True)

# Add a Label widget to the Frame
label = ttk.Label(frame, text="This is a label inside a frame.")
label.pack(pady=5)

# Add a Button widget to the Frame
button = ttk.Button(frame, text="Click Me")
button.pack(pady=5)

# Configure the Frame
frame.config(relief='sunken', borderwidth=2)

# Run the application
root.mainloop()