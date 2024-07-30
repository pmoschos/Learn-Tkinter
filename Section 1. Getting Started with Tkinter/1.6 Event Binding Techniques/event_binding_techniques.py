import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Event Binding Techniques Example")

# Function to handle button click
def on_button_click(event):
    print("Button clicked at coordinates ({}, {})".format(event.x, event.y))

# Create and pack a Button widget with click event binding
button = tk.Button(root, text="Click Me")
button.bind("<Button-1>", on_button_click)  # Bind left mouse button click
button.pack(pady=10)

# Function to handle key press event
def on_key_press(event):
    print("Key pressed: {}".format(event.keysym))

# Bind key press event to the main window
root.bind("<KeyPress>", on_key_press)

# Run the application
root.mainloop()