import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Spinbox Widget Example")

# Create and pack a Spinbox widget
spinbox = tk.Spinbox(root, from_=0, to=100)
spinbox.pack(pady=20)

# Function to show the spinbox value
def show_spinbox_value():
    print("Spinbox Value:", spinbox.get())

# Create and pack a Button to show the spinbox value
button = ttk.Button(root, text="Show Spinbox Value", command=show_spinbox_value)
button.pack(pady=10)

# Run the application
root.mainloop()