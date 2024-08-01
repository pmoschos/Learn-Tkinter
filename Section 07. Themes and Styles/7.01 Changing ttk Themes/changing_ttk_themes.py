import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.geometry('400x300')
root.title('Changing ttk Themes Demo')

# Create a style object
style = ttk.Style()

# Print available themes
print("Available themes:", style.theme_names())

# Set the theme
style.theme_use('clam')  # Change 'clam' to any available theme

# Create a label
label = ttk.Label(root, text="Hello, Tkinter!")
label.pack(pady=20)

# Create a button
button = ttk.Button(root, text="Click Me")
button.pack(pady=10)

# Run the application
root.mainloop()