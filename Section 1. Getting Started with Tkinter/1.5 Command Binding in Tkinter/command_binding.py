import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Command Binding Example")

# Function to handle button click
def on_button_click():
    print("Button clicked!")

# Create and pack a Button widget with command binding
button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=10)

# Function to handle button press event
def on_button_press(event):
    print("Button pressed!")

# Create and pack a Button widget with event binding
event_button = tk.Button(root, text="Press Me")
event_button.bind("<Button-1>", on_button_press)
event_button.pack(pady=10)

# Callback fumction assosiated with the ttk button command
ttk.Button(root, text="Callback", command=lambda: print("Callback")).pack()

# Run the application
root.mainloop()