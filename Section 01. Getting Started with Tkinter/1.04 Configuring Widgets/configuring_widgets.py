import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Configuring Widgets Example")

# Create and pack a Button widget with initial options
button = tk.Button(root, text="Click Me", fg="white", bg="blue")
button.pack(pady=10)

# Configure the Button widget's options later
# button.config(text="Press Me", fg="white", bg="red")

# Create and pack a Label widget with initial options
label = tk.Label(root, text="Hello, Tkinter!", font=("Helvetica", 16))
label.pack(pady=10)

# Configure the Label widget's options later
label.config(text="Hello, World!", font=("Arial", 20), fg="green")

# Function to change button text dynamically
def change_button_text():
    button.config(text="You Clicked Me!", bg="red")

# Create and pack a Button widget with dynamic configuration
dynamic_button = tk.Button(root, text="Click Me", command=change_button_text)
dynamic_button.pack(pady=10)

# Run the application
root.mainloop()