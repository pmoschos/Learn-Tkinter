import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Radio Button Widget Example")

# Variable to store the state of the selected radio button
selected_option = tk.StringVar(value="Option 1")

# Create and pack Radio Button widgets
radio1 = ttk.Radiobutton(root, text="Option 1", variable=selected_option, value="Option 1")
radio2 = ttk.Radiobutton(root, text="Option 2", variable=selected_option, value="Option 2")
radio3 = ttk.Radiobutton(root, text="Option 3", variable=selected_option, value="Option 3")

radio1.pack(pady=5)
radio2.pack(pady=5)
radio3.pack(pady=5)

# Function to show the selected option
def show_selected_option():
    print("Selected Option:", selected_option.get())

# Create and pack a Button to show the selected option
button = ttk.Button(root, text="Show Selected Option", command=show_selected_option)
button.pack(pady=10)

# Run the application
root.mainloop()