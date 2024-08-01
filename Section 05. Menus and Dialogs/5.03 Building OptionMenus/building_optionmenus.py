import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.geometry('400x300')
root.title('Building OptionMenus Demo')

# Define the variable to store the selected option
selected_option = tk.StringVar()
selected_option.set("Option 1")  # Set default value

# Create an OptionMenu widget
option_menu = ttk.OptionMenu(root, selected_option, "Option 1", "Option 1", "Option 2", "Option 3")
option_menu.pack(pady=20)

# Function to handle the selection of an option
def handle_selection(*args):
    print(f"Selected option: {selected_option.get()}")

# Bind the function to the variable
selected_option.trace("w", handle_selection)

# Run the application
root.mainloop()