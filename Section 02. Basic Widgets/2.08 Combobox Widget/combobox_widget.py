import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Combobox Widget Example")

# Variable to store the selected option
selected_option = tk.StringVar()

# Create and pack a Combobox widget
combobox = ttk.Combobox(root, textvariable=selected_option)
combobox['values'] = ("Option 1", "Option 2", "Option 3")
combobox.pack(pady=10)

# Function to show the selected option
def show_selected_option():
    print("Selected Option:", selected_option.get())

# Create and pack a Button to show the selected option
button = ttk.Button(root, text="Show Selected Option", command=show_selected_option)
button.pack(pady=10)

# Run the application
root.mainloop()