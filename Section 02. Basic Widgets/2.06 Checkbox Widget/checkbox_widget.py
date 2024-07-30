import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Checkbox Widget Example")

# Variable to store the state of the checkbox
checkbox_var = tk.BooleanVar()

# Create and pack a Checkbox widget
checkbox = ttk.Checkbutton(root, text="Accept Terms and Conditions", variable=checkbox_var)
checkbox.pack(pady=10)

# Function to show the state of the checkbox
def show_state():
    print("Checkbox State:", checkbox_var.get())

# Create and pack a Button to show the state of the checkbox
button = ttk.Button(root, text="Show State", command=show_state)
button.pack(pady=10)

# Run the application
root.mainloop()